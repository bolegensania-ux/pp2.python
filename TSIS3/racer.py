import pygame
import random
from persistence import save_score

class RacerGame:
    def __init__(self, player_name):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Racer Game")
        self.clock = pygame.time.Clock()

        self.player_name = player_name

        self.lanes = [120, 350, 580]

        self.current_lane = 1
        self.player = pygame.Rect(self.lanes[self.current_lane], 550, 60, 90)

        self.running = True

        self.traffic = []
        self.base_traffic_speed = 3
        self.traffic_speed = self.base_traffic_speed

        self.obstacles = []
        self.base_obstacle_speed = 2
        self.obstacle_speed = self.base_obstacle_speed

        self.spawn_rate = 1  # for scaling

        self.power_up = None
        self.power_type = None
        self.power_timer = 0

        self.distance = 0
        self.score = 0

        self.font = pygame.font.SysFont("Arial", 24)

    def run(self):
        while self.running:
            self.handle_events()

            # progression
            self.distance += 0.1
            self.score += 0.05

            
            if self.distance > 200:
                self.spawn_rate = 2
            if self.distance > 500:
                self.spawn_rate = 3

            self.spawn_traffic()
            self.update_traffic()

            self.spawn_obstacles()
            self.update_obstacles()

            self.spawn_power_up()
            self.update_power_up()

            
            if self.power_type == "nitro":
                if pygame.time.get_ticks() - self.power_timer > 4000:
                    self.traffic_speed = self.base_traffic_speed
                    self.obstacle_speed = self.base_obstacle_speed
                    self.power_type = None

            self.draw()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.current_lane > 0:
                    self.current_lane -= 1
                if event.key == pygame.K_RIGHT and self.current_lane < 2:
                    self.current_lane += 1

        self.player.x = self.lanes[self.current_lane]

    def draw(self):
        self.screen.fill((50, 50, 50))

        for lane in self.lanes:
            pygame.draw.line(self.screen, (255,255,255), (lane+30,0), (lane+30,700), 2)

        pygame.draw.rect(self.screen, (255,0,0), self.player)

        for car in self.traffic:
            pygame.draw.rect(self.screen, (0,0,255), car)

        for obs in self.obstacles:
            pygame.draw.rect(self.screen, (255,225,0), obs)

        if self.power_up:
            if self.power_type == "nitro":
                color = (0,255,255)
            elif self.power_type == "shield":
                color = (0,255,0)
            else:
                color = (255,255,0)

            pygame.draw.rect(self.screen, color, self.power_up)

        self.screen.blit(self.font.render(f"Score: {int(self.score)}", True, (255,255,255)), (10,10))
        self.screen.blit(self.font.render(f"Distance: {int(self.distance)}", True, (255,255,255)), (10,40))

        if self.power_type:
            self.screen.blit(self.font.render(f"Power: {self.power_type}", True, (255,255,255)), (10,70))

    def spawn_traffic(self):
        if random.randint(1,100) < self.spawn_rate:  
            lane = random.choice(self.lanes)
            self.traffic.append(pygame.Rect(lane, -80, 60, 90))

    def update_traffic(self):
        for car in self.traffic[:]:
            car.move_ip(0, self.traffic_speed)

            if car.top > 700:
                self.traffic.remove(car)

            if self.player.colliderect(car):
                save_score(self.player_name, self.score, self.distance)
                self.running = False

    def spawn_obstacles(self):
        if random.randint(1,100) < self.spawn_rate:
            lane = random.choice(self.lanes)
            self.obstacles.append(pygame.Rect(lane, -40, 60, 40))

    def update_obstacles(self):
        for obs in self.obstacles[:]:
            obs.move_ip(0, self.obstacle_speed)

            if obs.top > 700:
                self.obstacles.remove(obs)

            if self.player.colliderect(obs):
                save_score(self.player_name, self.score, self.distance)
                self.running = False

    def spawn_power_up(self):
        if self.power_up is None and random.randint(1,200) < 2:
            lane = random.choice(self.lanes)
            self.power_up = pygame.Rect(lane, -40, 40, 40)
            self.power_type = random.choice(["nitro","shield","repair"])

    def update_power_up(self):
        if self.power_up:
            self.power_up.move_ip(0,4)

            if self.power_up.top > 700:
                self.power_up = None

            elif self.player.colliderect(self.power_up):
                self.activate_power(self.power_type)
                self.power_up = None

    def activate_power(self, ptype):
        self.power_type = ptype

        if ptype == "nitro":
            self.traffic_speed = self.base_traffic_speed + 3
            self.obstacle_speed = self.base_obstacle_speed + 3
            self.power_timer = pygame.time.get_ticks()

        elif ptype == "shield":
            pass

        elif ptype == "repair":
            self.power_type = None