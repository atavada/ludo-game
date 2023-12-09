import pygame

class Buttons:
    def __init__(self, x, y, width, height, surface, acolor, pcolor, text, fontsize, function=None):
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
        self.click_sound = pygame.mixer.Sound('resources/audio/btn.mp3')
        # Tambahkan atribut rect
        self.rect = pygame.Rect(self.xcor, self.ycor, self.width, self.height)

    def Draw(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(self.surface, self.acolor, self.rect, border_radius=10)
            if self.func is not None and pygame.mouse.get_pressed()[0] == 1:
                # play click sound
                self.click_sound.play()
                self.func()
        else:
            pygame.draw.rect(self.surface, self.pcolor, self.rect, border_radius=10)

        if self.bname is not None:
            fontobj = pygame.font.Font('freesansbold.ttf', self.fontsize)
            displayfont = fontobj.render(self.bname, True, [255, 255, 255])
            disrect = displayfont.get_rect(center=(self.xcor + self.width / 2, self.ycor + self.height / 2))
            self.surface.blit(displayfont, disrect)
