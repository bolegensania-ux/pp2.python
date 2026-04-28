import pygame
import json

pygame.init()
font = pygame.font.SysFont("Arial", 30)

def draw_text(screen, text, x, y):
    txt = font.render(text, True, (255,255,255))
    rect = txt.get_rect(center=(x,y))
    screen.blit(txt, rect)
    return rect

def main_menu(screen):
    while True:
        screen.fill((30,30,30))

        play_btn = draw_text(screen, "PLAY", 400, 250)
        leader_btn = draw_text(screen, "LEADERBOARD", 400, 320)
        settings_btn = draw_text(screen, "SETTINGS", 400, 390)
        quit_btn = draw_text(screen, "QUIT", 400, 460)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"
                if leader_btn.collidepoint(event.pos):
                    return "leaderboard"
                if settings_btn.collidepoint(event.pos):
                    return "settings"
                if quit_btn.collidepoint(event.pos):
                    return "quit"

def leaderboard_screen(screen):
    try:
        with open("leaderboard.json") as f:
            data = json.load(f)
    except:
        data = []

    while True:
        screen.fill((20,20,20))
        draw_text(screen, "LEADERBOARD", 400, 100)

        y = 180
        for i, entry in enumerate(data):
            text = f"{i+1}. {entry['name']} - {entry['score']}"
            draw_text(screen, text, 400, y)
            y += 40

        back_btn = draw_text(screen, "BACK", 400, 600)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"

def settings_screen(screen):
    try:
        with open("settings.json") as f:
            settings = json.load(f)
    except:
        settings = {"sound": True, "difficulty": "medium"}

    while True:
        screen.fill((40,40,40))

        draw_text(screen, f"Sound: {settings['sound']}", 400, 250)
        draw_text(screen, f"Difficulty: {settings['difficulty']}", 400, 320)

        toggle_btn = draw_text(screen, "TOGGLE SOUND", 400, 400)
        back_btn = draw_text(screen, "BACK", 400, 500)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if toggle_btn.collidepoint(event.pos):
                    settings["sound"] = not settings["sound"]

                if back_btn.collidepoint(event.pos):
                    with open("settings.json", "w") as f:
                        json.dump(settings, f, indent=4)
                    return "menu"