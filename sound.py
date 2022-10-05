import pygame

class Sound():
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)
        self.is_played = False

    def play(self):
        if not self.is_played:
            self.sound.play()
            self.is_played = True

    def stop(self):
        self.sound.stop()

class SceneSound(Sound):
    def __init__(self, path, sound_num):
        self.index = 0
        self.sounds = []
        self.sound_num = sound_num
        self.path = path
        for i in range(self.sound_num):
            sound = Sound(self.path + str(i) + ".mp3")
            self.sounds.append(sound)
        self.now_sound = self.sounds[0]
        self.is_played = False

    def update(self):
        if(not self.is_played):
            self.index += 1
            if self.index >= len(self.sounds):
                self.is_played = True
                self.now_sound = None
                return
            else:
                self.now_sound.stop()

            self.now_sound = self.sounds[self.index]
    
    def backward(self):
        if self.index > 0:
            self.now_sound.stop()
            self.index -= 1
            self.now_sound = self.sounds[self.index]
    
    def play(self):
        if self.now_sound != None:
            self.now_sound.play()