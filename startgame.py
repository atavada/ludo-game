import pygame, sys
from Boardparameters import *
class board:
    def __init__(self, surface):
        self.surface = surface


    def createboard(self):
        def bx( x, y):
                pygame.draw.rect(self.surface, black, pygame.Rect(x, y, SBW, SBH), 1)

        def rd(x, y):
            pygame.draw.rect(self.surface, red, pygame.Rect(x, y, SBW, SBH))

        def grn(x, y):
            pygame.draw.rect(self.surface, green, pygame.Rect(x, y, SBW, SBH))

        def ylw(x, y,width = None):
            if width == None:
                pygame.draw.rect(self.surface, yellow, pygame.Rect(x, y, SBW, SBH))
            else:
                pygame.draw.rect(self.surface, yellow, pygame.Rect(x, y, SBW, SBH),width)

        def ble(x, y):
            pygame.draw.rect(self.surface, blue, pygame.Rect(x, y, SBW, SBH))

        # boardimage = pygame.image.load('resources\Ludo_board.jpg')
        # self.surface.blit(boardimage, (50, 50))
        pygame.draw.rect(self.surface, green, pygame.Rect(BXO, BYO, BBW, BBH))
        pygame.draw.rect(self.surface, red, pygame.Rect(BXO, BYO+3*SBH +BBH, BBW, BBH))
        pygame.draw.rect(self.surface, yellow, pygame.Rect(BXO+3*SBW+BBW, BYO, BBW, BBH))
        pygame.draw.rect(self.surface, blue, pygame.Rect(BXO+3*SBW+BBW, BYO+3*SBH+BBH, BBW, BBH))

        pygame.draw.rect(self.surface, white, pygame.Rect(30+BXO, 30+BYO, BIBW, BIBH))
        pygame.draw.rect(self.surface, white, pygame.Rect(30+BXO, 30+BYO+3*SBH +BBH, BIBW, BIBH))
        pygame.draw.rect(self.surface, white, pygame.Rect(30+BXO+3*SBW+BBW, 30+BYO, BIBW, BIBH))
        pygame.draw.rect(self.surface, white, pygame.Rect(30+BXO+3*SBW+BBW, 30+BYO+3*SBH+BBH, BIBW, BIBH))

        pygame.draw.rect(self.surface, green, pygame.Rect(30 + BXO, 76 + BYO, TPBW, TPBW),2)
        pygame.draw.rect(self.surface, green, pygame.Rect(2*TPBW +30 + BXO, 76 + BYO, TPBW, TPBW),2)
        pygame.draw.rect(self.surface, green, pygame.Rect(30+TPBW + BXO, 30 + BYO, TPBW, TPBW),2)
        pygame.draw.rect(self.surface, green, pygame.Rect(30+ TPBW+ BXO, 2*TPBW+30 + BYO, TPBW, TPBW),2)

        pygame.draw.rect(self.surface, red, pygame.Rect(30 + BXO, 76 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, red, pygame.Rect(76+ BXO, 30 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, red, pygame.Rect(30+ 2*TPBW  + BXO, 76 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, red, pygame.Rect(30 + TPBW  +BXO, 30 + 2*TPBW + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)

        pygame.draw.rect(self.surface, yellow, pygame.Rect(30 + BXO + 3 * SBW + BBW,TPBW + 30 + BYO, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, yellow, pygame.Rect(TPBW + 30 + BXO + 3 * SBW + BBW, 30 + BYO, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, yellow, pygame.Rect(2*TPBW + 30 + BXO + 3 * SBW + BBW, TPBW + 30 + BYO, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, yellow, pygame.Rect(TPBW + 30 + BXO + 3 * SBW + BBW, 2*TPBW+30 + BYO, TPBW, TPBW), 2)

        pygame.draw.rect(self.surface, blue, pygame.Rect(30 + BXO + 3 * SBW + BBW, TPBW +30 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, blue, pygame.Rect(30 + TPBW + BXO + 3 * SBW + BBW, 30 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, blue, pygame.Rect(30 + TPBW +BXO + 3 * SBW + BBW, 2*TPBW + 30 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)
        pygame.draw.rect(self.surface, blue, pygame.Rect(2*TPBW + 30 + BXO + 3 * SBW + BBW, TPBW +30 + BYO + 3 * SBH + BBH, TPBW, TPBW), 2)

        pygame.draw.polygon(self.surface,green,[T1, T3, T4])
        pygame.draw.polygon(self.surface, yellow, [T1, T3, T2])
        pygame.draw.polygon(self.surface, red, [T4, T3, T5])
        pygame.draw.polygon(self.surface, blue, [T2, T3, T5])

        for i in range(5):
            grn(axis[1+i], axis[7])
            rd(axis[7], axis[9+i])
            ble(axis[9 + i], axis[7])
            ylw(axis[7], axis[1 + i])
        ylw(axis[6],axis[2])
        ylw(axis[8],axis[1])
        grn(axis[2],axis[8])
        grn(axis[1],axis[6])
        rd(axis[8],axis[12])
        rd(axis[6],axis[13])
        ble(axis[13],axis[8])
        ble(axis[12],axis[6])

        for i in range(3):
            for j in range(6):
                bx(axis[6+i], axis[j])
                bx(axis[j],axis[6+i])
                bx(axis[6+i],axis[9+j])
                bx(axis[9+j],axis[6+i])

