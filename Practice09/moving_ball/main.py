import pygame
import ball

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
              ball.move(0, -ball.STEP)
           if event.key == pygame.K_DOWN:
              ball.move(0, ball.STEP)
           if event.key == pygame.K_LEFT:
              ball.move(-ball.STEP, 0)
           if event.key == pygame.K_RIGHT:
              ball.move(ball.STEP, 0)

    screen.fill((255, 255, 255))  # white background

    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()