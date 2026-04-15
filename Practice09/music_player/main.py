import pygame
from player import play, stop, track, current

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            if event.key == pygame.K_s:
                stop()
                running = False

    screen.fill((32, 26, 110))

    # show current track
    text = font.render("Track: track1.mp3", True, (255, 255, 255))
    screen.blit(text, (50, 180))

    pygame.display.flip()

pygame.quit()