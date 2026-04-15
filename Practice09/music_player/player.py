import pygame

track = ["Practice09/music_player/music/track1.mp3"]

current = 0

def play():
    pygame.mixer.music.load(track[current])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

