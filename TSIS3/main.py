import pygame
from racer import RacerGame
from ui import main_menu, leaderboard_screen, settings_screen

pygame.init()
screen = pygame.display.set_mode((800,700))

while True:
    choice = main_menu(screen)

    if choice == "play":
        name = input("Enter your name: ")
        game = RacerGame(name)
        game.run()

    elif choice == "leaderboard":
        leaderboard_screen(screen)

    elif choice == "settings":
        settings_screen(screen)

    elif choice == "quit":
        break

pygame.quit()