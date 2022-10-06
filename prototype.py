import pygame
import button
import setting

class Prototype():
    def __init__(self):
        self.title = pygame.image.load("img/ending/prototype/Ending_GameLogo.png")
        self.title = pygame.transform.scale(self.title, (701/2, 226/2))
        self.dev_team = pygame.image.load("img/ending/prototype/DevTeamCredit.png")
        self.dev_team = pygame.transform.scale(self.dev_team, (114/2, 360/2))
        self.thanks = pygame.image.load("img/ending/prototype/ThanksForPlaying.png")
        self.thanks = pygame.transform.scale(self.thanks, (1071/2, 139/2))
        self.back = pygame.image.load("img/background.png")
        self.back = pygame.transform.scale(self.back, (800, 600))
        self.restart = button.RestartButton()

    def render(self):
        setting.screen.blit(self.back, (0, 0))
        setting.screen.blit(self.title, (450/2, 169/2))
        setting.screen.blit(self.dev_team, (1396/2, 711/2))
        setting.screen.blit(self.thanks, (265/2, 461/2))

        self.restart.show()
        