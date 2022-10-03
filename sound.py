import pygame

class Sound():
    def __init__(self):
        self.sound = None

    def load_sound(self, path):
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        self.sound.play()
