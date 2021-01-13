import pygame, sys
from pygame.locals import *

class Label():
    def __init__(self, win, text, color, x, y, fontSize = 50):
        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', fontSize)
        
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.win = win

    def drawLetter(self):
        self.label = self.mainFont.render(self.text, 1, self.color)
        self.win.blit(self.label, (self.x, self.y))

class Button():
    def __init__(self, win, color, x, y, width, height, text = '', textColor = (255, 255, 255), textSize = 50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.text = text
        self.textColor = textColor
        self.textSize = textSize

    def checkCollision(self, mousePos):
        col = pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mousePos)
        if col == 1:
            return True
        else:
            return False
        
    def drawButton(self):
        pygame.font.init()
        font = pygame.font.SysFont('comicsans', self.textSize)
        text = font.render(self.text, 1, self.textColor)
        text_rect = text.get_rect(center=pygame.Rect(self.x, self.y, self.width, self.height).center)
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))
        self.win.blit(text, text_rect)