# add tools
import pygame
pygame.init()

#window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill("WHITE")

tool = "pen"
color = BLACK
radius = 5
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
               tool = "pen"
            if event.key == pygame.K_2:
               tool = "rect"
            if event.key == pygame.K_3:
               tool = "circle"
            if event.key == pygame.K_4:
               tool = "eraser"

            if event.key == pygame.K_r:
               color = (255, 0, 0)
            if event.key == pygame.K_g:
               color = (0, 255, 0)
            if event.key == pygame.K_b:
               color = (0, 0, 255)
            if event.key == pygame.K_k:
               color = (0, 0, 0)

        # save the starting position
        if event.type == pygame.MOUSEBUTTONDOWN:
           start_pos = event.pos

        # draw shapes
        if event.type == pygame.MOUSEBUTTONUP:
           end_pos = event.pos

           if tool == "rect":
                rect = pygame.Rect(start_pos,
                                   (end_pos[0] - start_pos[0],
                                    end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)

           if tool == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 +
                              (end_pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    #  DRAW WHILE HOLDING MOUSE
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()

        if tool == "pen":
            pygame.draw.circle(screen, color, mouse_pos, radius)

        if tool == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
