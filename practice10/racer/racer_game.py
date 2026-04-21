import pygame
import random

pygame.init()

clock = pygame.time.Clock()

# set a window for a game

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Racer Game")

# adding our object
object1 = pygame.Rect(180, 500, 40, 60)
speed = 3

# adding the enemy 
enemy = pygame.Rect(random.randint(0, 760), 0, 40, 60)
enemy_speed = 2

# adding coins that need to be collected
coin = pygame.Rect(random.randint(0, 780), 0, 20, 20)
coin_speed = 3
score = 0

font = pygame.font.SysFont("Arial", 24)

# set the loop that runs the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        object1.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT]:
        object1.move_ip(speed, 0)
    
     # move enemy
    enemy.move_ip(0, enemy_speed)

    # reset enemy
    if enemy.top > 700:
        enemy.top = 0
        enemy.left = random.randint(0, 760)

    # collision
    if object1.colliderect(enemy):
        print("Game Over")
        running = False

    # make coin fall
    coin.move_ip(0, coin_speed)

    # reset the coin
    if coin.top > 700:
        coin.top = 0
        coin.left = random.randint(0, 780)

    # collision wirh coins
    if object1.colliderect(coin):
        score += 1
        coin.top = 0
        coin.left = random.randint(0, 780)

    # background color
    screen.fill((255, 181, 192))
    # our object in the screen
    pygame.draw.rect(screen, (255, 0, 0), object1)
    pygame.draw.rect(screen, (0, 0, 0), enemy)
    pygame.draw.circle(screen, (255, 255, 0), coin.center, 10)
    text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(text, (650, 10))
    # update the screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()