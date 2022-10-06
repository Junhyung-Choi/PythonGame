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

    def add_sound(self, path, sound_num):
        for i in range(sound_num):
            sound = Sound(path + str(i) + ".mp3")
            self.sounds.append(sound)

class SceneSounds():
    def __init__(self, path, sound_num):
        self.sounds = []
        self.path = path
        self.sound_num = sound_num
        self.index = 0
        for i in range(self.sound_num):
            sound = Sound(self.path + str(i) + ".mp3")
            self.sounds.append(sound)
    
    def update(self, b):
        if self.index < self.sound_num and b:
            if self.sounds[self.index] != None:
                self.sounds[self.index].stop()
                self.sounds[self.index].is_played = False
            self.index += 1
            
    def backward(self, b):
        if self.index > 0 and b:
            if self.sounds[self.index] != None:
                self.sounds[self.index].stop()
                self.sounds[self.index].is_played = False
            self.index -= 1

    def add_sound(self, path, sound_num):
        self.sound_num += sound_num
        for i in range(sound_num):
            sound = Sound(path + str(i) + ".mp3")
            self.sounds.append(sound)
        
    def add_None(self):
        self.sound_num += 1
        self.sounds.append(None)

    def play(self):
        if self.sounds[self.index] != None:
            self.sounds[self.index].play()
    
    def stop(self):
        self.sounds[self.index].stop()