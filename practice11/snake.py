import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)

# food
food = (200, 200)

# food with different value
food_val = random.choice([1, 3, 5])

# adding food timer
food_timer = pygame.time.get_ticks()
food_lifetime = 5000

score = 0
level = 1
speed = 3

font = pygame.font.SysFont("Arial", 24)

# main loop starts
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -20)
            if event.key == pygame.K_DOWN:
                direction = (0, 20)
            if event.key == pygame.K_LEFT:
                direction = (-20, 0)
            if event.key == pygame.K_RIGHT:
                direction = (20, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)


    # check collision with walls
    if (head[0] < 0 or head[0] >= 800 or
        head[1] < 0 or head[1] >= 700):
        print("Game Over")
        running = False


     # check collision with itself
    if head in snake[1:]:
        print("Game Over")
        running = False


     # check if snake eats food
    if head == food:
        score += food_val
        level = score // 2 + 1
        # generate new food (random position)
        food = (random.randrange(0, 800, 20),
                random.randrange(0, 700, 20))
        food_val =  random.choice([1, 3, 5])
        food_timer = pygame.time.get_ticks()
    else:
        snake.pop()

    #if it takes too long to get to the food, it generates again at random position
    current_time = pygame.time.get_ticks()
    if current_time - food_timer > food_lifetime:
       food = (random.randrange(0, 800, 20),
               random.randrange(0, 700, 20))
       food_val = random.choice([1, 3, 5])
       food_timer = pygame.time.get_ticks()


    screen.fill((255, 0, 255))


    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))

    if food_val == 1:
        color = (255, 0, 0)
    elif food_val == 3:
        color = (0, 0, 255)
    else:
        color = (255, 215, 0)
    pygame.draw.rect(screen, color, (*food, 20, 20))

    random.randrange(0, 800, 20)


    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))

    screen.blit(text, (10, 10))

    pygame.display.update()

    speed = 10 + (level * 2)
    clock.tick(speed)

pygame.quit()