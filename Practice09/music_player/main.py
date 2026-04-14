import pygame
from player import play, stop, next_track, prev_track, track, current

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
            if event.key == pygame.K_n:
                next_track()
            if event.key == pygame.K_b:
                prev_track()
            if event.key == pygame.K_q:
                running = False

    screen.fill((0, 0, 0))

    # show current track
    text = font.render(f"Track: {track[current]}", True, (255, 255, 255))
    screen.blit(text, (50, 180))

    pygame.display.flip()

pygame.quit()