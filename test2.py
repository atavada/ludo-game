import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *  # modul OpenGL.GLU digunakan untuk membuat perspektif
from pygame.locals import *
import buttons
import startgame
import random
import player
from pygame.mouse import get_pos as pos
from coordinates import *
import pygame.sysfont
from dice import *
import os
import asyncio

# set pygame screen
pygame.init()
pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)
pygame.display.init()
info = pygame.display.Info()
bgimage = pygame.image.load("resources/bg.jpg")
screen = pygame.Surface((info.current_w, info.current_h))
# center the screen
os.environ["SDL_VIDEO_CENTERED"] = "1"


###button colors##
pcolor = [46, 64, 83]
acolor = [52, 73, 94]
pred = [231, 76, 60]
ared = [236, 112, 99]
agreen = [82, 190, 128]
pgreen = [39, 174, 96]
ablue = [93, 173, 226]
pblue = [52, 152, 219]
ayellow = [244, 208, 63]
pyellow = [241, 196, 15]
###

# basic opengl configuration
glViewport(0, 0, info.current_w, info.current_h)
glDepthRange(0, 1)
glMatrixMode(GL_PROJECTION)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glShadeModel(GL_SMOOTH)
glClearColor(0.0, 0.0, 0.0, 0.0)
glClearDepth(1.0)
glDisable(GL_DEPTH_TEST)
glDisable(GL_LIGHTING)
glDepthFunc(GL_LEQUAL)
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
glEnable(GL_BLEND)

###
### Function to convert a PyGame Surface to an OpenGL Texture
### Maybe it's not necessary to perform each of these operations
### every time.
###
texID = glGenTextures(1)
# create pygame clock
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 30)  # some default font


done = False


def surfaceToTexture(pygame_surface):
    global texID
    rgb_surface = pygame.image.tostring(pygame_surface, "RGB")
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    surface_rect = pygame_surface.get_rect()
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGB,
        surface_rect.width,
        surface_rect.height,
        0,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        rgb_surface,
    )
    glGenerateMipmap(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)


###Token buttons##
pcrd = [
    buttons.Buttons(600, 50, 100, 50, screen, ared, pred, "Token 1", 14, function=None),
    buttons.Buttons(
        600, 150, 100, 50, screen, ared, pred, "Token 2", 14, function=None
    ),
    buttons.Buttons(
        600, 250, 100, 50, screen, ared, pred, "Token 3", 14, function=None
    ),
    buttons.Buttons(
        600, 350, 100, 50, screen, ared, pred, "Token 4", 14, function=None
    ),
]

pcgrn = [
    buttons.Buttons(
        600, 50, 100, 50, screen, agreen, pgreen, "Token 1", 14, function=None
    ),
    buttons.Buttons(
        600, 150, 100, 50, screen, agreen, pgreen, "Token 2", 14, function=None
    ),
    buttons.Buttons(
        600, 250, 100, 50, screen, agreen, pgreen, "Token 3", 14, function=None
    ),
    buttons.Buttons(
        600, 350, 100, 50, screen, agreen, pgreen, "Token 4", 14, function=None
    ),
]

pcylw = [
    buttons.Buttons(
        600, 50, 100, 50, screen, ayellow, pyellow, "Token 1", 14, function=None
    ),
    buttons.Buttons(
        600, 150, 100, 50, screen, ayellow, pyellow, "Token 2", 14, function=None
    ),
    buttons.Buttons(
        600, 250, 100, 50, screen, ayellow, pyellow, "Token 3", 14, function=None
    ),
    buttons.Buttons(
        600, 350, 100, 50, screen, ayellow, pyellow, "Token 4", 14, function=None
    ),
]

pcble = [
    buttons.Buttons(
        600, 50, 100, 50, screen, ablue, pblue, "Token 1", 14, function=None
    ),
    buttons.Buttons(
        600, 150, 100, 50, screen, ablue, pblue, "Token 2", 14, function=None
    ),
    buttons.Buttons(
        600, 250, 100, 50, screen, ablue, pblue, "Token 3", 14, function=None
    ),
    buttons.Buttons(
        600, 350, 100, 50, screen, ablue, pblue, "Token 4", 14, function=None
    ),
]

diceimg = {
    1: pygame.image.load("resources\dice1.png"),
    2: pygame.image.load("resources\dice2.png"),
    3: pygame.image.load("resources\dice3.png"),
    4: pygame.image.load("resources\dice4.png"),
    5: pygame.image.load("resources\dice5.png"),
    6: pygame.image.load("resources\dice6.png"),
}
###

###Token initiation
Player = {
    0: (
        player.player(green, screen, "1"),
        player.player(green, screen, "2"),
        player.player(green, screen, "3"),
        player.player(green, screen, "4"),
    ),
    1: (
        player.player(yellow, screen, "1"),
        player.player(yellow, screen, "2"),
        player.player(yellow, screen, "3"),
        player.player(yellow, screen, "4"),
    ),
    2: (
        player.player(blue, screen, "1"),
        player.player(blue, screen, "2"),
        player.player(blue, screen, "3"),
        player.player(blue, screen, "4"),
    ),
    3: (
        player.player(red, screen, "1"),
        player.player(red, screen, "2"),
        player.player(red, screen, "3"),
        player.player(red, screen, "4"),
    ),
}
##

### Start game parameters
sts = 0
draw = 0
turn = 0
position = {
    0: [-1, -1, -1, -1],
    1: [-1, -1, -1, -1],
    2: [-1, -1, -1, -1],
    3: [-1, -1, -1, -1],
}
playerturn = 0
firstdraw = [
    True,
    True,
    True,
    True,
]
tokenclick = True
diceclick = False


###
# each player 4 token state
# -1 = not in game
# 0-56 = position in game
# 57 = win
# 58 = home
###button function##


def newgame():
    global sts
    sts = 1


def exit():
    pygame.quit()
    sys.exit()


def quitgame():
    global sts, position, playerturn, tokenclick, diceclick, firstdraw, draw
    draw = 0
    sts = 0
    position = {
        0: [-1, -1, -1, -1],
        1: [-1, -1, -1, -1],
        2: [-1, -1, -1, -1],
        3: [-1, -1, -1, -1],
    }
    playerturn = 0
    tokenclick = True
    diceclick = False
    firstdraw = [
        True,
        True,
        True,
        True,
    ]


def Throw():
    global draw, tokenclick, diceclick, spinning
    if tokenclick == True:
        draw = random.randint(1, 6)
        tokenclick = False
        diceclick = True
        print(spinning)
        start(draw)
        CleanupGL()


###

###button object###
newbtn = buttons.Buttons(
    250, 300, 100, 50, screen, acolor, pcolor, "New Game", 16, newgame
)
exitbtn = buttons.Buttons(250, 400, 100, 50, screen, acolor, pcolor, "Exit", 16, exit)
quitbtn = buttons.Buttons(
    400, 10, 100, 30, screen, acolor, pcolor, "Quit Game", 14, quitgame
)
quitbtn1 = buttons.Buttons(
    350, 450, 100, 50, screen, acolor, pcolor, "Quit Game", 14, quitgame
)
dicebtn = buttons.Buttons(
    100, 10, 100, 30, screen, acolor, pcolor, "Throw Dice", 14, Throw
)
###


###game function##3
def UpBoard():
    for i in range(4):
        for j in range(4):
            if position[i][j] == -1:
                if i == 0:
                    Player[0][j].draw(greenorigin[j][0], greenorigin[j][1])
                if i == 1:
                    Player[1][j].draw(yelloworigin[j][0], yelloworigin[j][1])
                if i == 2:
                    Player[2][j].draw(blueorigin[j][0], blueorigin[j][1])
                if i == 3:
                    Player[3][j].draw(redorigin[j][0], redorigin[j][1])
            else:
                if i == 0:
                    Player[0][j].draw(
                        GreenPath[position[i][j]][0], GreenPath[position[i][j]][1]
                    )
                if i == 1:
                    Player[1][j].draw(
                        YellowPath[position[i][j]][0], YellowPath[position[i][j]][1]
                    )
                if i == 2:
                    Player[2][j].draw(
                        BluePath[position[i][j]][0], BluePath[position[i][j]][1]
                    )
                if i == 3:
                    Player[3][j].draw(
                        RedPath[position[i][j]][0], RedPath[position[i][j]][1]
                    )


def pcd(player):
    pygame.draw.rect(screen, white, pygame.Rect(600, 450, 100, 50))
    fontobj = pygame.font.Font("freesansbold.ttf", 18)
    if player == 0:
        displayfont = fontobj.render("Player 1", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 1:
        displayfont = fontobj.render("Player 2", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 2:
        displayfont = fontobj.render("Player 3", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 3:
        displayfont = fontobj.render("Player 4", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)


def PlayerTokenSelect(player):
    global draw, firstdraw, playerturn
    if player == 0:
        if draw == 6 or firstdraw[player] == True:
            for i in range(4):
                pcgrn[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcgrn[i].Draw()
        pcd(player)
    if player == 1:
        if draw == 6 or firstdraw[player] == True:
            for i in range(4):
                pcylw[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcylw[i].Draw()
        pcd(player)
    if player == 2:
        if draw == 6 or firstdraw[player] == True:
            for i in range(4):
                pcble[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcble[i].Draw()
        pcd(player)
    if player == 3:
        if draw == 6 or firstdraw[player] == True:
            for i in range(4):
                pcrd[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcrd[i].Draw()
        pcd(player)


def CollisionChecker(pt, token):
    global position
    if pt == 0 and position[pt][token] != -1:
        if (
            position[pt][token] != 8
            and position[pt][token] != 21
            and position[pt][token] != 34
            and position[pt][token] != 47
        ):
            for i in range(4):
                if GreenPath.get(position[pt][token]) == YellowPath.get(position[1][i]):
                    position[1][i] = -1
                if GreenPath.get(position[pt][token]) == BluePath.get(position[2][i]):
                    position[2][i] = -1
                if GreenPath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 1 and position[pt][token] != -1:
        if (
            position[pt][token] != 8
            and position[pt][token] != 21
            and position[pt][token] != 34
            and position[pt][token] != 47
        ):
            for i in range(4):
                if YellowPath.get(position[pt][token]) == GreenPath.get(position[0][i]):
                    position[0][i] = -1
                if YellowPath.get(position[pt][token]) == BluePath.get(position[2][i]):
                    position[2][i] = -1
                if YellowPath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 2 and position[pt][token] != -1:
        if (
            position[pt][token] != 8
            and position[pt][token] != 21
            and position[pt][token] != 34
            and position[pt][token] != 47
        ):
            for i in range(4):
                if BluePath.get(position[pt][token]) == GreenPath.get(position[0][i]):
                    position[0][i] = -1
                if BluePath.get(position[pt][token]) == YellowPath.get(position[1][i]):
                    position[1][i] = -1
                if BluePath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 3 and position[pt][token] != -1:
        if (
            position[pt][token] != 8
            and position[pt][token] != 21
            and position[pt][token] != 34
            and position[pt][token] != 47
        ):
            for i in range(4):
                if RedPath.get(position[pt][token]) == GreenPath.get(position[0][i]):
                    position[0][i] = -1
                if RedPath.get(position[pt][token]) == YellowPath.get(position[1][i]):
                    position[1][i] = -1
                if RedPath.get(position[pt][token]) == BluePath.get(position[2][i]):
                    position[2][i] = -1


def randomZone(pt, token):
    # if player land in
    if pt == 0 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            # set the token to random zone
            position[pt][token] = random.randint(0, 56)

    elif pt == 1 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(0, 56)

    elif pt == 2 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(0, 56)

    elif pt == 3 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(0, 56)


def playerchoice():
    global playerturn, diceclick, tokenclick, position, draw
    if diceclick == True:
        if playerturn == 4:
            playerturn = 0

        if 700 >= pos()[0] >= 600 and 100 >= pos()[1] >= 50:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][0] += 1
                        firstdraw[playerturn] = False

                elif (
                    position[playerturn][0] + draw < 57
                    and position[playerturn][0] != -1
                ):
                    position[playerturn][0] += draw

                elif position[playerturn][0] == -1 and draw == 6:
                    position[playerturn][0] += 1
                CollisionChecker(playerturn, 0)
                randomZone(playerturn, 0)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 200 >= pos()[1] >= 150:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][1] += 1
                        firstdraw[playerturn] = False
                elif (
                    position[playerturn][1] + draw < 57
                    and position[playerturn][1] != -1
                ):
                    position[playerturn][1] += draw
                elif position[playerturn][1] == -1 and draw == 6:
                    position[playerturn][1] += 1

                CollisionChecker(playerturn, 1)
                randomZone(playerturn, 1)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 300 >= pos()[1] >= 250:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][2] += 1
                        firstdraw[playerturn] = False
                elif (
                    position[playerturn][2] + draw < 57
                    and position[playerturn][2] != -1
                ):
                    position[playerturn][2] += draw
                elif position[playerturn][2] == -1 and draw == 6:
                    position[playerturn][2] += 1
                CollisionChecker(playerturn, 2)
                randomZone(playerturn, 2)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 400 >= pos()[1] >= 350:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][3] += 1
                        firstdraw[playerturn] = False
                elif (
                    position[playerturn][3] + draw < 57
                    and position[playerturn][3] != -1
                ):
                    position[playerturn][3] += draw
                elif position[playerturn][3] == -1 and draw == 6:
                    position[playerturn][3] += 1
                CollisionChecker(playerturn, 3)
                randomZone(playerturn, 3)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1


def win():
    if (
        position[0][0] == 56
        and position[0][1] == 56
        and position[0][2] == 56
        and position[0][3] == 56
    ):
        return True
    elif (
        position[1][0] == 56
        and position[1][1] == 56
        and position[1][2] == 56
        and position[1][3] == 56
    ):
        return True
    elif (
        position[2][0] == 56
        and position[2][1] == 56
        and position[2][2] == 56
        and position[2][3] == 56
    ):
        return True
    elif (
        position[3][0] == 56
        and position[3][1] == 56
        and position[3][2] == 56
        and position[3][3] == 56
    ):
        return True
    return False


def showwin(ply):
    fontobj = pygame.font.Font("freesansbold.ttf", 35)
    screen.fill((255, 255, 255))
    if ply == 4:
        ply = 0
    if ply == 0:
        displayfont = fontobj.render("player green won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 1:
        displayfont = fontobj.render("Player Yellow won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 2:
        displayfont = fontobj.render("Player Blue won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 3:
        displayfont = fontobj.render("Player Red won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
    quitbtn1.Draw()


sex = 0
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    # Do all the PyGame operations to the offscreen surface
    if sts == 0:
        screen.blit(bgimage, (0, 0))
        newbtn.Draw()
        exitbtn.Draw()

    if sts == 1:
        screen.fill((255, 255, 255))
        newgame = startgame.board(screen)
        newgame.createboard()
        quitbtn.Draw()
        dicebtn.Draw()
        if draw == 0:
            if sex == 57:
                sex = 0
            Player[0][1].draw(GreenPath[sex][0], GreenPath[sex][1])
            Player[1][1].draw(YellowPath[sex][0], YellowPath[sex][1])
            Player[2][1].draw(BluePath[sex][0], BluePath[sex][1])
            Player[3][1].draw(RedPath[sex][0], RedPath[sex][1])

            sex += 1
            for i in range(4):
                Player[0][i].draw(greenorigin[i][0], greenorigin[i][1])
                Player[1][i].draw(yelloworigin[i][0], yelloworigin[i][1])
                Player[2][i].draw(blueorigin[i][0], blueorigin[i][1])
                Player[3][i].draw(redorigin[i][0], redorigin[i][1])

        else:
            if win() == False:
                screen.blit(diceimg[draw], (275, 0))
                UpBoard()
                PlayerTokenSelect(playerturn)
                playerchoice()
            elif win() == True:
                showwin(playerturn)

    # prepare to render the texture-mapped rectangle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)

    # Draw texture-mapped rectangle
    surfaceToTexture(screen)
    glBindTexture(GL_TEXTURE_2D, texID)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -1)
    glTexCoord2f(1, 1)
    glVertex2f(1, -1)
    glTexCoord2f(1, 0)
    glVertex2f(1, 1)
    glEnd()

    # create rect inthe middle of the screen using opengl 0.
    # glDisable(GL_TEXTURE_2D)
    # glLoadIdentity()
    # glLineWidth(1)
    # glColor3f(1, 1, 1)
    # glBegin(GL_QUADS)
    # glVertex2f(-0.1, 0.1)
    # glVertex2f(-0.1, -0.1)
    # glVertex2f(0.1, -0.1)
    # glVertex2f(0.1, 0.1)
    # glEnd()
    # wait for some time

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
