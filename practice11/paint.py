"""
to draw recangular/square: 

square = pygame.Rect(x, y, width, height)

pygame.draw.rect(screen, (0, 0, 255), sqaure) ---> inside the main loop

"""

"""
to draw triangular:

triangle = [(x1, y1), (x2, y2), (x3, y3)]    ---> we store only points

pygame.draw.polygon(screen, color, triangle) ---> inside the loop  

 # we use "polygon" for creating triangulars and rhombus
"""

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
screen.fill(WHITE)

shape = "rect"   # current shape
running = True
drawing = False

start_pos = (0, 0)
end_pos = (0, 0)

color = (0, 0, 0)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🔹 KEYBOARD (MUST be inside loop)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rect"
            elif event.key == pygame.K_s:
                shape = "square"
            elif event.key == pygame.K_t:
                shape = "triangle"
            elif event.key == pygame.K_e:
                shape = "equilateral"
            elif event.key == pygame.K_d:
                shape = "rhombus"

        # 🔹 MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

    # 🔹 update position while dragging
    if drawing:
        end_pos = pygame.mouse.get_pos()

    x1, y1 = start_pos
    x2, y2 = end_pos

    width = x2 - x1
    height = y2 - y1

    # 🔹 clear screen
    screen.fill(WHITE)

    # 🔹 draw shapes ONLY when dragging
    if drawing:
        if shape == "rect":
            pygame.draw.rect(screen, color, (x1, y1, width, height), 3)

        elif shape == "square":
            pygame.draw.rect(screen, color, (x1, y1, height, height), 3)

        elif shape == "triangle":
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y2), (x2, y2)], 3)

        elif shape == "equilateral":
            mid_x = (x1 + x2) // 2
            pygame.draw.polygon(screen, color, [(mid_x, y1), (x1, y2), (x2, y2)], 3)

        elif shape == "rhombus":
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            pygame.draw.polygon(screen, color, [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)], 3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()