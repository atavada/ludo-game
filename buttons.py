import pygame, sys
class Buttons:
    def __init__(self, x, y, width, height, surface, acolor, pcolor, text, fontsize, function = None):
        self.xcor = x
        self.ycor = y
        self.bname = text
        self.width = width
        self.height = height
        self.surface = surface
        self.acolor = acolor
        self.pcolor = pcolor
        self.fontsize = fontsize
        self.func = function

    def Draw(self):
        mouse = pygame.mouse.get_pos()
        if (self.xcor+self.width) >= mouse[0] >= self.xcor and (self.ycor+self.height) >= mouse[1] >= self.ycor:
            pygame.draw.rect(self.surface, self.acolor, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
            if self.func != None:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.func()
        else:
            pygame.draw.rect(self.surface, self.pcolor, pygame.Rect(self.xcor, self.ycor, self.width, self.height))

        if self.bname != None:
            fontobj = pygame.font.Font('freesansbold.ttf', self.fontsize)
            displayfont = fontobj.render(self.bname, True, [255, 255, 255])
            disrect = displayfont.get_rect()
            disrect.center = (self.xcor + self.width/2, self.ycor + self.height/2 )
            self.surface.blit(displayfont, disrect)
