import pygame, random, json

def run_game(best):

    pygame.init()
    screen = pygame.display.set_mode((800,700))
    clock = pygame.time.Clock()

    # --- settings ---
    try:
        with open("settings.json") as f:
            s = json.load(f)
    except:
        s = {"snake_color":[0,255,0],"grid":False,"sound":False}

    snake_color = tuple(s["snake_color"])
    grid = s["grid"]

    snake=[(100,100),(80,100),(60,100)]
    direction=(20,0)

    food=(200,200)
    food_val=random.choice([1,3,5])
    poison=(400,400)

    power=None
    ptype=None
    ptime=0
    active=None
    end=0
    shield=False

    obstacles=[]

    score=0
    level=1

    running=True
    while running:
        t=pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction!=(0,20): direction=(0,-20)
        if keys[pygame.K_DOWN] and direction!=(0,-20): direction=(0,20)
        if keys[pygame.K_LEFT] and direction!=(20,0): direction=(-20,0)
        if keys[pygame.K_RIGHT] and direction!=(-20,0): direction=(20,0)

        head=(snake[0][0]+direction[0],snake[0][1]+direction[1])
        snake.insert(0,head)

        if head[0]<0 or head[0]>=800 or head[1]<0 or head[1]>=700:
            if shield: shield=False
            else: running=False

        if head in snake[1:]:
            if shield: shield=False
            else: running=False

        if level>=3 and len(obstacles)<level*3:
            obstacles=[]
            for _ in range(level*3):
                while True:
                    b=(random.randrange(0,800,20),random.randrange(0,700,20))
                    if b not in snake:
                        obstacles.append(b); break

        if head in obstacles:
            if shield: shield=False
            else: running=False

        if head==food:
            score+=food_val
            level=score//2+1
            food=(random.randrange(0,800,20),random.randrange(0,700,20))
            food_val=random.choice([1,3,5])
        else:
            snake.pop()

        if head==poison:
            if len(snake)>2:
                snake.pop(); snake.pop()
            else: running=False
            poison=(random.randrange(0,800,20),random.randrange(0,700,20))

        if power is None and random.randint(1,200)==1:
            power=(random.randrange(0,800,20),random.randrange(0,700,20))
            ptype=random.choice(["speed","slow","shield"])
            ptime=t

        if power and t-ptime>8000:
            power=None

        if power and head==power:
            active=ptype
            end=t+5000
            power=None
            if active=="shield": shield=True

        if active and t>end:
            active=None

        screen.fill((255,0,255))

        if grid:
            for x in range(0,800,20):
                pygame.draw.line(screen,(200,200,200),(x,0),(x,700))
            for y in range(0,700,20):
                pygame.draw.line(screen,(200,200,200),(0,y),(800,y))

        for s in snake:
            pygame.draw.rect(screen,snake_color,(*s,20,20))

        pygame.draw.rect(screen,(255,0,0),(*food,20,20))
        pygame.draw.rect(screen,(139,0,0),(*poison,20,20))

        for b in obstacles:
            pygame.draw.rect(screen,(100,100,100),(*b,20,20))

        if power:
            c=(255,255,0) if ptype=="speed" else (0,255,255) if ptype=="slow" else (255,255,255)
            pygame.draw.rect(screen,c,(*power,20,20))

        font=pygame.font.SysFont(None,24)
        txt=font.render(f"Score:{score} Level:{level} Best:{best}",True,(255,255,255))
        screen.blit(txt,(10,10))

        pygame.display.update()

        base=min(15,8+level)
        if active=="speed": speed=base+5
        elif active=="slow": speed=max(5,base-3)
        else: speed=base

        clock.tick(speed)

    # save settings
    with open("settings.json","w") as f:
        json.dump({"snake_color":list(snake_color),"grid":grid,"sound":False},f,indent=4)

    pygame.quit()
    return score, level