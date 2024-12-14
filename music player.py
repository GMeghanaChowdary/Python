import pygame
def music_player():
    pygame.mixer.init()
    song = input("Enter song file path: ")
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
music_player()
