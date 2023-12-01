import pygame
import tokens

class player:
    def __init__(self, color, surface ,num):
        self.color = color
        self.surface = surface
        self.num = num
    def draw(self, x, y):
        self.xcor = x
        self.ycor = y
        dice = tokens.systoken(self.xcor, self.ycor, self.surface, self.color, self.num)
        dice.draw()

