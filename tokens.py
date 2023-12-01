import pygame
'''class token:
    def __init__(self, x, y, surface, color):
        self.xcor = x
        self.ycor = y
        self.screen = surface
        self.color = color
    def draw(self):
        if self.color == 'red':
            image = pygame.image.load('resources\Red.png')
        elif self.color == 'green':
            image = pygame.image.load('resources\Green.png')
        elif self.color == 'yellow':
            image = pygame.image.load('resources\Yellow.png')
        elif self.color == 'blue':
            image = pygame.image.load('resources\Blue.png')
        self.screen.blit(image, (self.xcor, self.ycor))'''
class systoken:
    def __init__(self, x, y, surface, color, tnum):
        self.xcen = x
        self.ycen = y
        self.surf = surface
        self.clr = color
        self.num = tnum
    def draw(self):
        pygame.draw.circle(self.surf, self.clr, (self.xcen, self.ycen), 15, 0)
        pygame.draw.circle(self.surf, [0, 0, 0], (self.xcen, self.ycen), 15, 1)
        fontobj = pygame.font.Font('freesansbold.ttf', 14)
        displayfont = fontobj.render(self.num, True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (self.xcen, self.ycen)
        self.surf.blit(displayfont, disrect)







