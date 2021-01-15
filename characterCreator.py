import pygame, sys
from pygame.locals import *

class Character():
    def __init__(self, win, x, y, picture):
        self.win = win
        self.x = x
        self.y = y
        self.picture = picture
        self.name = None
        self.maxHP = 10
        self.aktHP = 10
        self.maxEP = 10
        self.aktEP = 10
        self.maxXP = 10
        self.aktXP = 0
        self.Level = 1
        self.phyDamage = 2
        self.intDamage = 2
        self.vel = 10

    def LevelUp(self):
        self.maxHP += 1
        self.maxEP += 1
        self.maxXP += 1
        self.phyDamage += 1
        self.intDamage += 1
        self.Level += 1

    def xpGain(self, gainedXP):
        self.aktXP += gainedXP
        if self.aktXP >= self.maxXP:
            self.aktXP -= self.maxXP
            self.LevelUp()
        
    def drawCharacter(self):
        self.characterpicture = pygame.image.load(self.picture)
        self.win.blit(self.characterpicture, (self.x, self.y))

    def getCharacterWidth(self):
        return self.characterpicture.get_rect().size[0]

    def getCharacterHeight(self):
        return self.characterpicture.get_rect().size[1]

    def characterToRect(self):
        filler = pygame.Rect(self.x, self.y, self.getCharacterWidth(), self.getCharacterHeight())
        return filler