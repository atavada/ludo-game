import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import startgame
import buttons
import random
import player
from pygame.mouse import get_pos as pos
from coordinates import *
import pygame.sysfont
import os
import textwrap
from dice import start, CleanupGL

# main screen
pygame.init()
pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)
pygame.display.init()
info = pygame.display.Info()
bgimage = pygame.image.load("resources/bg.jpg")
screen = pygame.Surface((info.current_w, info.current_h))
pygame.display.set_caption("LUDOang")
icon = pygame.image.load("resources/icon/icon.png")
pygame.display.set_icon(icon)
os.environ["SDL_VIDEO_CENTERED"] = "1"

# button colors
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


# pion buttons
pcrd = [
    buttons.Buttons(600, 50, 100, 50, screen, ared, pred, "Pion 1", 14, function=None),
    buttons.Buttons(600, 110, 100, 50, screen, ared, pred, "Pion 2", 14, function=None),
    buttons.Buttons(600, 170, 100, 50, screen, ared, pred, "Pion 3", 14, function=None),
    buttons.Buttons(600, 230, 100, 50, screen, ared, pred, "Pion 4", 14, function=None),
    # skip button
    buttons.Buttons(600, 290, 100, 50, screen, ared, pred, "Skip", 14, function=None),
]

pcgrn = [
    buttons.Buttons(
        600, 50, 100, 50, screen, agreen, pgreen, "Pion 1", 14, function=None
    ),
    buttons.Buttons(
        600, 110, 100, 50, screen, agreen, pgreen, "Pion 2", 14, function=None
    ),
    buttons.Buttons(
        600, 170, 100, 50, screen, agreen, pgreen, "Pion 3", 14, function=None
    ),
    buttons.Buttons(
        600, 230, 100, 50, screen, agreen, pgreen, "Pion 4", 14, function=None
    ),
    #  skip button
    buttons.Buttons(
        600, 290, 100, 50, screen, agreen, pgreen, "Skip", 14, function=None
    ),
]

pcylw = [
    buttons.Buttons(
        600, 50, 100, 50, screen, ayellow, pyellow, "Pion 1", 14, function=None
    ),
    buttons.Buttons(
        600, 110, 100, 50, screen, ayellow, pyellow, "Pion 2", 14, function=None
    ),
    buttons.Buttons(
        600, 170, 100, 50, screen, ayellow, pyellow, "Pion 3", 14, function=None
    ),
    buttons.Buttons(
        600, 230, 100, 50, screen, ayellow, pyellow, "Pion 4", 14, function=None
    ),
    #  skip button
    buttons.Buttons(
        600, 290, 100, 50, screen, ayellow, pyellow, "Skip", 14, function=None
    ),
]

pcble = [
    buttons.Buttons(
        600, 50, 100, 50, screen, ablue, pblue, "Pion 1", 14, function=None
    ),
    buttons.Buttons(
        600, 110, 100, 50, screen, ablue, pblue, "Pion 2", 14, function=None
    ),
    buttons.Buttons(
        600, 170, 100, 50, screen, ablue, pblue, "Pion 3", 14, function=None
    ),
    buttons.Buttons(
        600, 230, 100, 50, screen, ablue, pblue, "Pion 4", 14, function=None
    ),
    #  skip button
    buttons.Buttons(600, 290, 100, 50, screen, ablue, pblue, "Skip", 14, function=None),
]

diceimg = {
    1: pygame.image.load("resources\dice1.png"),
    2: pygame.image.load("resources\dice2.png"),
    3: pygame.image.load("resources\dice3.png"),
    4: pygame.image.load("resources\dice4.png"),
    5: pygame.image.load("resources\dice5.png"),
    6: pygame.image.load("resources\dice6.png"),
}

# pion initiation
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

# start game parameters
sts = -1
draw = 0
turn = 0
###
# each player 4 token state
# -1 = not in game
# 0-56 = position in game
# 57 = win
# 58 = home
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


###button function##
def newgame():
    global sts
    sts = 1
    # stop soundtrack
    pygame.mixer.music.stop()
    # play new soundtrack
    music_list = [
        "resources/audio/ingame_1.mp3",
        "resources/audio/ingame_2.mp3",
    ]
    pygame.mixer.music.load(random.choice(music_list))
    # decrase volume
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)


def exit():
    pygame.quit()
    sys.exit()


def back_function():
    global sts
    pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)
    pygame.Surface((info.current_w, info.current_h))
    sts = 0


def rules_function():
    r_screen = pygame.display.set_mode((800, 600), DOUBLEBUF)
    r_screen.fill((255, 255, 255))
    title_font = pygame.font.Font("freesansbold.ttf", 32)
    title_text = title_font.render("Peraturan Permainan Ludo", True, [0, 0, 0])
    title_rect = title_text.get_rect(center=(400, 40))

    rule_text = [
        "Peraturan Permainan LUDOang",
        "",
        "Persiapan Permainan:",
        "- Papan permainan Ludo memiliki jalur yang terbagi menjadi empat warna: merah, kuning, hijau, dan biru.",
        "- Setiap pemain memiliki empat buah pion dalam warna yang sesuai.",
        "- Pions ditempatkan di rumah masing-masing pemain di ujung jalur.",
        "",
        "Tujuan Permainan:",
        "- Pemain pertama yang berhasil membawa keempat pionnya ke pusat papan permainan adalah pemenangnya.",
        "",
        "Aturan Pergeseran Pion:",
        "- Pion dapat bergerak sejauh jumlah mata dadu yang dilempar.",
        "- Jika dadu menunjukkan enam, pemain dapat melempar lagi dan bergerak pion baru atau memindahkan pion yang sudah bergerak.",
        "- Pion hanya dapat diakses oleh pemain yang memiliki warna yang sesuai dengan warna jalur yang diikuti.",
        "",
        "Aturan Keamanan (Safe Zone):",
        "- Kotak yang ditempati oleh pion sendiri adalah zona aman. Pion di zona aman tidak dapat dihentikan oleh pemain lain.",
        "- Pemain lain tidak dapat melewati zona aman pemain lainnya.",
        "",
        "Aturan Memakan Pion Pemain Lain:",
        "- Jika pion mendarat di kotak yang sudah ditempati oleh pion pemain lain, pion pemain lain tersebut dipindahkan kembali ke rumahnya.",
        "",
        "Aturan Masuk ke Pusat:",
        "- Untuk memasukkan pion ke pusat papan, pemain harus melempar dadu dan mendapatkan jumlah mata yang sesuai dengan jarak yang tersisa menuju pusat.",
        "- Pemain harus melempar jumlah mata yang pas untuk menyelesaikan perjalanan ke pusat.",
        "",
        "Aturan Dadu:",
        "- Dadu dilempar dengan menekan tombol 'Throw Dice'.",
        "- Jika dadu jatuh di luar papan atau tidak jelas, pemain harus melempar ulang.",
        "",
        "Pemenang:",
        "- Pemain yang pertama kali membawa keempat pionnya ke pusat papan adalah pemenangnya.",
    ]

    fontobj = pygame.font.Font("freesansbold.ttf", 20)
    max_width = 700  # Set the maximum width for text
    line_height = 25
    y_position = 50
    scroll_speed = 10  # Set the scroll speed

    scroll_y = 0

    back_btn_rules = buttons.Buttons(
        350,
        550,
        100,
        50,
        r_screen,
        (255, 0, 0),
        (200, 0, 0),
        "Back",
        16,
        back_function,
    )

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scroll_y += scroll_speed
                elif event.key == pygame.K_DOWN:
                    scroll_y -= scroll_speed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:  # Mouse wheel scroll up
                    scroll_y += scroll_speed
                elif event.button == 4:  # Mouse wheel scroll down
                    scroll_y -= scroll_speed
                elif back_btn_rules.rect.collidepoint(pygame.mouse.get_pos()):
                    waiting = False

        # Draw the title "Peraturan Permainan Ludo" with scrolling
        r_screen.fill((255, 255, 255))

        for line in rule_text:
            words = line.split(" ")
            lines = [""]
            current_line = 0

            for word in words:
                if fontobj.size(lines[current_line] + word)[0] <= max_width:
                    lines[current_line] += word + " "
                else:
                    current_line += 1
                    lines.append(word + " ")

            for formatted_line in lines:
                display_font = fontobj.render(formatted_line.rstrip(), True, [0, 0, 0])
                display_rect = display_font.get_rect(topleft=(50, y_position))
                r_screen.blit(display_font, display_rect)
                y_position += line_height

        # Adjust y_position based on scrolling
        y_position = 50 - scroll_y

        back_btn_rules.Draw()

        pygame.display.flip()


def about_function():
    about_screen = pygame.display.set_mode((800, 600), DOUBLEBUF)
    pygame.display.set_caption("LUDO GAME")

    title_font = pygame.font.Font("freesansbold.ttf", 32)
    title_text = title_font.render("About Us", True, [0, 0, 0])
    title_rect = title_text.get_rect(center=(400, 40))

    developer_profiles = [
        {
            "nama": "Alvalen Shafelbilyunazra",
            "nim": "220535608548",
            "photo": "Foto_Almet_Alvalen.png",
            "offering": "TI - A",
        },
        {
            "nama": "Ardha A. P. Agustavada",
            "nim": "220535608503",
            "photo": "Foto_Almet_Ardha.png",
            "offering": "TI - A",
        },
        {
            "nama": "Azarya A. K. Moeljono",
            "nim": "220535608951",
            "photo": "Azarya_Foto_Almet.png",
            "offering": "TI - A",
        },
        # Tambahkan profil pengembang lainnya sesuai kebutuhan
    ]

    fontobj = pygame.font.Font("freesansbold.ttf", 20)
    line_height = 30
    y_position = 100

    max_height = 450
    scroll_speed = 10
    scroll_y = 0

    back_btn_about = buttons.Buttons(
        350,
        550,
        100,
        50,
        about_screen,
        (255, 0, 0),
        (200, 0, 0),
        "Back",
        16,
        back_function,
    )

    description_text = "LUDOang adalah game ludo digital yang dibuat dengan menggunakan bahasa pemrograman python yang didukung oleh open gl, dan py game. Terinspirasi dari ludo konvensional, LUDOang dikembangkan agar menjadi lebih interaktif dan menarik. Berbeda dengan game ludo pada umumnya, LUDOang memiliki fitur unik yaitu random zone dimana ketika pion berada dalam petak atau zone tersebut, maka pion akan berpindah tempat secara acak."

    lorem_font = pygame.font.Font("freesansbold.ttf", 16)
    description_lines = textwrap.wrap(description_text, width=85)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel scroll up
                    scroll_y += scroll_speed
                elif event.button == 5:  # Mouse wheel scroll down
                    scroll_y -= scroll_speed
                elif back_btn_about.rect.collidepoint(pygame.mouse.get_pos()):
                    waiting = False

        about_screen.fill((255, 255, 255))

        # Draw the title "About Us" with scrolling
        about_screen.blit(title_text, (400 - title_rect.width // 2, 40 + scroll_y))

        # Draw the description text with scrolling
        for line in description_lines:
            description_rendered = lorem_font.render(line, True, [0, 0, 0])
            about_screen.blit(description_rendered, (50, y_position + scroll_y))
            y_position += line_height

        y_position += 20  # Jarak antara deskripsi dan profile

        # Draw the developer profiles with scrolling
        for profile in developer_profiles:
            photo_path = os.path.join("resources", profile["photo"])
            developer_image = pygame.image.load(photo_path)
            developer_image = pygame.transform.scale(developer_image, (85, 85))
            about_screen.blit(developer_image, (100, y_position + scroll_y))

            text_lines = [
                f"{key.capitalize()} : {value}"
                for key, value in profile.items()
                if key not in ["photo", "offering"]
            ]
            for line in text_lines:
                display_font = fontobj.render(line, True, [0, 0, 0])
                display_rect = display_font.get_rect(
                    topleft=(200, y_position + scroll_y)
                )
                about_screen.blit(display_font, display_rect)
                y_position += line_height

            offering_text = f"Offering : {profile['offering']}"
            display_font = fontobj.render(offering_text, True, [0, 0, 0])
            display_rect = display_font.get_rect(topleft=(200, y_position + scroll_y))
            about_screen.blit(display_font, display_rect)
            y_position += line_height  # Jarak antara Offering dan profil

            y_position += 30  # Jarak antara setiap profil

        y_position = 100  # Reset y_position

        # Draw the "Back" button
        back_btn_about.Draw()

        pygame.display.flip()


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
    pygame.mixer.music.stop()
    soundtracklist = [
        "resources/audio/soundtrack1.mp3",
        "resources/audio/soundtrack2.mp3",
    ]
    load = random.choice(soundtracklist)
    pygame.mixer.music.load(load)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)


def Throw():
    global draw, tokenclick, diceclick
    if tokenclick == True:
        draw = random.randint(1, 6)
        tokenclick = False
        diceclick = True
        dice_sound = pygame.mixer.Sound("resources/audio/dice.mp3")
        dice_sound.play()
        start(draw)
        CleanupGL()


# button object
newbtn = buttons.Buttons(
    350, 250, 100, 50, screen, agreen, pgreen, "New Game", 16, newgame
)
rules_btn = buttons.Buttons(
    350, 330, 100, 50, screen, ayellow, pyellow, "Rules", 16, rules_function
)
about_btn = buttons.Buttons(
    350, 410, 100, 50, screen, ablue, pblue, "About", 16, about_function
)
exitbtn = buttons.Buttons(350, 490, 100, 50, screen, ared, pred, "Exit", 16, exit)
quitbtn = buttons.Buttons(
    400, 10, 100, 30, screen, acolor, pcolor, "Quit Game", 14, quitgame
)
quitbtn1 = buttons.Buttons(
    350, 450, 100, 50, screen, acolor, pcolor, "Quit Game", 14, quitgame
)
dicebtn = buttons.Buttons(
    100, 10, 100, 30, screen, acolor, pcolor, "Throw Dice", 14, Throw
)


# game function
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
            for i in range(5):
                pcgrn[i].Draw()
        else:
            for i in range(5):
                if i < 4:
                    if position[player][i] != -1:
                        pcgrn[i].Draw()
        pcd(player)
    if player == 1:
        if draw == 6 or firstdraw[player] == True:
            for i in range(5):
                pcylw[i].Draw()
        else:
            for i in range(5):
                if i < 4:
                    if position[player][i] != -1:
                        pcylw[i].Draw()
        pcd(player)
    if player == 2:
        if draw == 6 or firstdraw[player] == True:
            for i in range(5):
                pcble[i].Draw()
        else:
            for i in range(5):
                if i < 4:
                    if position[player][i] != -1:
                        pcble[i].Draw()
        pcd(player)
    if player == 3:
        if draw == 6 or firstdraw[player] == True:
            for i in range(5):
                pcrd[i].Draw()
        else:
            for i in range(5):
                if i < 4:
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


# if player land in, randomize position
def randomZone(pt, token):
    if pt == 0 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            # set the token to random zone
            position[pt][token] = random.randint(-1, 56)

    elif pt == 1 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(-1, 56)

    elif pt == 2 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(-1, 56)

    elif pt == 3 and position[pt][token] != -1:
        if (
            position[pt][token] == 5
            or position[pt][token] == 18
            or position[pt][token] == 31
            or position[pt][token] == 44
        ):
            position[pt][token] = random.randint(-1, 56)


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

                randomZone(playerturn, 0)
                CollisionChecker(playerturn, 0)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 170 >= pos()[1] >= 110:
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
                randomZone(playerturn, 1)
                CollisionChecker(playerturn, 1)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 230 >= pos()[1] >= 170:
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
                randomZone(playerturn, 2)
                CollisionChecker(playerturn, 2)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1

        elif 700 >= pos()[0] >= 600 and 290 >= pos()[1] >= 230:
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
                randomZone(playerturn, 3)
                CollisionChecker(playerturn, 3)
                diceclick = False
                tokenclick = True
                if draw != 6:
                    playerturn += 1
        # skip button to skip turn
        elif 700 >= pos()[0] >= 600 and 350 >= pos()[1] >= 290:
            if pygame.mouse.get_pressed()[0] == 1:
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
    ply -= 1
    if ply == -1:
        ply = 3
    global screen
    fontobj = pygame.font.Font("freesansbold.ttf", 35)
    screen.fill((255, 255, 255))
    if ply == 4:
        ply = 0
    if ply == 0:
        screen.fill((0, 255, 0))
        displayfont = fontobj.render("player green won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
        # set color screen to green

    elif ply == 1:
        screen.fill((255, 255, 0))
        displayfont = fontobj.render("Player Yellow won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
        # set color screen to yellow

    elif ply == 2:
        screen.fill((0, 0, 255))
        displayfont = fontobj.render("Player Blue won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
        #  set color screen to blue

    elif ply == 3:
        screen.fill((255, 0, 0))
        displayfont = fontobj.render("Player Red won", True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
        # set color screen to red

    quitbtn1.Draw()


def loading_screen():
    global diceimg, sts
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF)
    screen.fill((255, 255, 255))
    frames = [diceimg[1], diceimg[2], diceimg[3], diceimg[4], diceimg[5], diceimg[6]]
    for frame in frames:
        window_width, window_height = pygame.display.get_surface().get_size()
        frame_width, frame_height = frame.get_size()
        center_x = (window_width - frame_width) // 2
        center_y = (window_height - frame_height) // 2
        screen.blit(frame, (center_x, center_y))
        pygame.display.flip()
        pygame.time.wait(500)
    pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)


soundtracklist = [
    "resources/audio/soundtrack1.mp3",
    "resources/audio/soundtrack2.mp3",
]
load = random.choice(soundtracklist)
pygame.mixer.music.load(load)
# play
pygame.mixer.music.play(-1)

loading = 0
random_tips = [
    "We Also Create Mini Harbor Game!",
    "Jangan Lupa Bernafas!",
    "Jangan Lupa Makan!",
    "Jangan Lupa Tidur!",
    "Furi indonesia! Solid Solid Solid",
    "YNTKTS",
    "Jangan Lupa Mandi!",
    "Jangan Lupa Sholat!",
    "Jangan Lupa Berdoa!",
    "Jangan Lupa Bersyukur!",
    "Minimal Maksimal",
]

# show showwin screen
tips = random.choice(random_tips)
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        # if mouse click up
        if event.type == pygame.MOUSEBUTTONUP and sts == -1 and loading > 1:
            # play click sound
            click_sound = pygame.mixer.Sound("resources/audio/btn.mp3")
            click_sound.play()
            loading_screen()
            sts = 0

    if sts == -1:
        splash = pygame.image.load("resources/bg.jpg")
        screen.blit(splash, (0, 0))
        if loading > 1:
            # Add message "Tap to continue" with outline
            fontobj = pygame.font.Font("freesansbold.ttf", 18)
            displayfont_outline = fontobj.render(
                "Tap to continue", True, [0, 0, 0]
            )  # Outline color
            displayfont = fontobj.render(
                "Tap to continue", True, [255, 255, 255]
            )  # Text color

            # Render the outline text
            disrect_outline = displayfont_outline.get_rect()
            disrect_outline.center = (400, 350)
            screen.blit(
                displayfont_outline, disrect_outline.move(2, 2)
            )  # Offset the outline text slightly

            # Render the main text
            disrect = displayfont.get_rect()
            disrect.center = (400, 350)
            screen.blit(displayfont, disrect)

        fontobj = pygame.font.Font("freesansbold.ttf", 18)

        # Render the outline text
        displayfont_outline = fontobj.render(tips, True, (0, 0, 0))  # Outline color
        disrect_outline = displayfont_outline.get_rect()
        disrect_outline.center = (400, 540)
        screen.blit(
            displayfont_outline, disrect_outline.move(2, 2)
        )  # Offset the outline text slightly

        # Render the main text
        displayfont = fontobj.render(tips, True, (255, 255, 255))  # Text color
        disrect = displayfont.get_rect()
        disrect.center = (400, 540)
        screen.blit(displayfont, disrect)

        if loading < 0.4:
            loading += 0.01
        elif loading < 0.8:
            loading += 0.005
        else:
            loading += 0.001
        # draw fake loading bar
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 500, 400, 20))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200, 500, 400, 20), 2)

        if loading < 1:
            pygame.draw.rect(
                screen, (255, 255, 255), pygame.Rect(200, 500, 400 * loading, 20)
            )
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200, 500, 400, 20))

    if sts == 0:
        # if audio not playing, play
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play(-1)

        screen.blit(bgimage, (0, 0))
        newbtn.Draw()
        rules_btn.Draw()
        about_btn.Draw()
        exitbtn.Draw()

    if sts == 1:
        screen.fill((255, 255, 255))
        newgame = startgame.board(screen)
        newgame.createboard()
        quitbtn.Draw()
        dicebtn.Draw()
        if draw == 0:
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

    # draw texture-mapped rectangle
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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
