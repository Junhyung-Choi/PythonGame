import pygame

class Sound():
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        self.sound.play()

class SceneSound(Sound):
    def __init__(self, path, sound_num):
        self.index = 0
        self.sounds = []
        self.sound_num = sound_num
        self.path = path
        for i in range(self.sound_num):
            sound = pygame.mixer.Sound(self.path + str(i) + ".mp3")
            self.sounds.append(sound)
        self.now_sound = self.sounds[0]
        self.is_played = False

    def update(self):
        if(not self.is_played):
            self.now_sound.stop()
            self.index += 1
            if self.index >= len(self.sounds):
                self.is_played = True
                self.now_sound = None
                return
            self.now_sound = self.sounds[self.index]
    
    def play(self):
        self.now_sound.play()