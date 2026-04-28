import pygame
import datetime
from tools import flood_fill

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

canvas = pygame.Surface((800, 800))
canvas.fill(WHITE)

shape = "rect"
running = True
drawing = False

start_pos = (0, 0)
end_pos = (0, 0)

color = (0, 0, 0)
brush_size = 3

last_pos = None

# text tool
font = pygame.font.SysFont(None, 30)
typing = False
text = ""
text_pos = (0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD
        if event.type == pygame.KEYDOWN:

            # shapes
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
            elif event.key == pygame.K_p:
                shape = "pencil"
            elif event.key == pygame.K_l:
                shape = "line"
            elif event.key == pygame.K_f:
                shape = "fill"
            elif event.key == pygame.K_x:
                shape = "text"
            elif event.key == pygame.K_c:
                shape = "eraser"

            # brush size
            elif event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            # save
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            # TEXT INPUT
            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    canvas.blit(img, text_pos)
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode

        # MOUSE DOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            end_pos = event.pos

            if shape == "fill":
                flood_fill(canvas, event.pos, color)

            elif shape == "text":
                typing = True
                text = ""
                text_pos = event.pos

            else:
                drawing = True
                last_pos = event.pos

        # MOUSE UP
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos
            width = x2 - x1
            height = y2 - y1

            # final draw to canvas
            if shape == "line":
                pygame.draw.line(canvas, color, start_pos, end_pos, brush_size)

            elif shape == "rect":
                pygame.draw.rect(canvas, color, (x1, y1, width, height), brush_size)

            elif shape == "square":
                pygame.draw.rect(canvas, color, (x1, y1, height, height), brush_size)

            elif shape == "triangle":
                pygame.draw.polygon(canvas, color, [(x1,y1),(x1,y2),(x2,y2)], brush_size)

            elif shape == "equilateral":
                mid_x = (x1+x2)//2
                pygame.draw.polygon(canvas, color, [(mid_x,y1),(x1,y2),(x2,y2)], brush_size)

            elif shape == "rhombus":
                mid_x = (x1+x2)//2
                mid_y = (y1+y2)//2
                pygame.draw.polygon(canvas, color,
                                    [(mid_x,y1),(x2,mid_y),(mid_x,y2),(x1,mid_y)],
                                    brush_size)

        # MOUSE DRAG
        if drawing:
            end_pos = pygame.mouse.get_pos()

            if shape == "pencil":
                pygame.draw.line(canvas, color, last_pos, end_pos, brush_size)
                last_pos = end_pos

            elif shape == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, end_pos, brush_size)

    # PREVIEW
    if drawing and shape != "pencil":
        temp = canvas.copy()

        x1, y1 = start_pos
        x2, y2 = end_pos
        width = x2 - x1
        height = y2 - y1

        if shape == "line":
            pygame.draw.line(temp, color, start_pos, end_pos, brush_size)

        elif shape == "rect":
            pygame.draw.rect(temp, color, (x1,y1,width,height), brush_size)

        elif shape == "square":
            pygame.draw.rect(temp, color, (x1,y1,height,height), brush_size)

        elif shape == "triangle":
            pygame.draw.polygon(temp, color, [(x1,y1),(x1,y2),(x2,y2)], brush_size)

        elif shape == "equilateral":
            mid_x = (x1+x2)//2
            pygame.draw.polygon(temp, color, [(mid_x,y1),(x1,y2),(x2,y2)], brush_size)

        elif shape == "rhombus":
            mid_x = (x1+x2)//2
            mid_y = (y1+y2)//2
            pygame.draw.polygon(temp, color,
                                [(mid_x,y1),(x2,mid_y),(mid_x,y2),(x1,mid_y)],
                                brush_size)

        screen.blit(temp, (0,0))

    else:
        screen.blit(canvas, (0,0))

    # TEXT PREVIEW
    if typing:
        temp = canvas.copy()
        img = font.render(text, True, color)
        temp.blit(img, text_pos)
        screen.blit(temp, (0,0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()