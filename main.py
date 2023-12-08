import pygame
import sys
import startgame
import buttons
import random
import player
from pygame.mouse import get_pos as pos
from coordinates import *
import pygame.sysfont


pygame.init()
###main screen##
size = width, height = 800, 600
bgimage = pygame.image.load("resources/bg.jpg")
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crap")
###

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
    clock = pygame.time.Clock()
    global draw, tokenclick, diceclick    
    frames = []
    if tokenclick == True:
        draw = random.randint(1, 6)
        frames = [diceimg[i] for i in range(1, 7)]
        tokenclick = False
        diceclick = True
    
    size = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255)) 

    for frame in frames:
        window_width, window_height = pygame.display.get_surface().get_size()
        frame_width, frame_height = frame.get_size()
        center_x = (window_width - frame_width) // 2
        center_y = (window_height - frame_height) // 2
        screen.blit(frame, (center_x, center_y)) 
        pygame.display.flip()
        pygame.time.wait(500)
    pygame.display.flip()
    
    clock.tick(2)
    # time.sleep(3)
###

###button object###
newbtn = buttons.Buttons(350, 250, 100, 50, screen, agreen, pgreen, 'New Game', 16, newgame)
exitbtn = buttons.Buttons(350, 330, 100, 50, screen, ared, pred, 'Exit', 16, exit)
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
                elif position[playerturn][0] == -1 and draw == 6:
                    position[playerturn][0] += 1

                CollisionChecker(playerturn, 1)
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
                CollisionChecker(playerturn, 2)
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

###Actual Loop
while True:
    pygame.display.flip()
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
