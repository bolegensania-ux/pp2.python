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
        score += 1
        level = score // 2 + 1
        # generate new food (random position)
        food = (random.randrange(0, 800, 20),
                random.randrange(0, 700, 20))
    else:
        snake.pop()

    screen.fill((255, 0, 255))


    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))


    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))
    random.randrange(0, 800, 20)


    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))

    screen.blit(text, (10, 10))

    pygame.display.update()

    speed = 10 + (level * 2)
    clock.tick(speed)

pygame.quit()