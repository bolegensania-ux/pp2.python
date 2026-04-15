import pygame
from clock import get_angles

pygame.init()

screen = pygame.display.set_mode((600, 600))
hand = pygame.image.load("Practice09/mickeys_clock/images/mickey_clock.jpeg")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sec_angle, min_angle = get_angles()

    screen.fill((255, 255, 255))

    sec_hand = pygame.transform.rotate(hand, -sec_angle)
    min_hand = pygame.transform.rotate(hand, -min_angle)

    screen.blit(sec_hand, sec_hand.get_rect(center=(300, 300)))
    screen.blit(min_hand, min_hand.get_rect(center=(300, 300)))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()