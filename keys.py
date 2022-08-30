# importing pygame

import pygame

pygame.mixer.init()

# To off music
def music_of():
    pygame.mixer.music.stop()

# TO on music
def music_play():
    pygame.mixer.music.load("Sneaky-Snitch.mp3")
    pygame.mixer.music.play(loops=-1)
