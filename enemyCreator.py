import pygame, sys
from pygame.locals import *
from resource import *





Schüler = [studentPicture, "Schüler", 10, 10, 1, 1]
Lehrer = [teacherPicture, "Lehrer", 10, 10, 1, 1]
#Test = ()
#Klausur = ()

class Enemy():
    def __init__(self, win, x, y, picture, name, maxHP, aktHP, level, phyDamage):
        self.win = win
        self.picture = picture
        self.name = name
        self.maxHP = maxHP
        self.aktHP = aktHP
        self.xp = 20
        self.level = level
        self.phyDamage = phyDamage
        self.x = x
        self.y = y
        self.enemypicture = pygame.image.load(self.picture)
        self.enemypicture = pygame.transform.scale(self.enemypicture, (300, 300))
        
    def drawEnemy(self, x, y):   
        self.win.blit(self.enemypicture, (x, y))
    
    def takeDamage(self, damage):
        self.aktHP -= damage


#enemy1 = Enemy(Schüler[0], Schüler[1], Schüler[2], Schüler[3], Schüler[4], Schüler[5])
#print(enemy1.maxHP)


