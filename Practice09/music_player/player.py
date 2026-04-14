import pygame

track = ["music/track1.mp3"]

current = 0

def play():
    pygame.mixer.music.load(track[current])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current
    current = (current + 1) % len(track)
    play()

def prev_track():
    global current
    current = (current - 1) % len(track)
    play()