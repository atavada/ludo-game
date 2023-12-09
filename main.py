import pygame
import sys
import startgame
import buttons
import random
import player
from pygame.mouse import get_pos as pos
from coordinates import *
import  pygame.sysfont
import os
import textwrap

pygame.init()
###main screen##
size = width, height = 800, 600
bgimage = pygame.image.load('resources/bg.jpg')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('LUDO GAME')
###

###button colors##
pcolor  = [46, 64, 83]
acolor  = [52, 73, 94]
pred     = [231, 76, 60]
ared    =[236, 112, 99]
agreen = [82, 190, 128]
pgreen = [39, 174, 96]
ablue = [93, 173, 226]
pblue =[52, 152, 219]
ayellow = [244, 208, 63]
pyellow = [241, 196, 15]
###

###Token buttons##
pcrd = [buttons.Buttons(600, 50, 100, 50, screen, ared, pred, 'Token 1',14,function=None),
             buttons.Buttons(600, 150, 100, 50, screen, ared, pred, 'Token 2',14,function=None),
             buttons.Buttons(600, 250, 100, 50, screen, ared, pred, 'Token 3',14,function=None),
             buttons.Buttons(600, 350, 100, 50, screen, ared, pred, 'Token 4',14,function=None)]

pcgrn= [buttons.Buttons(600, 50, 100, 50, screen, agreen, pgreen, 'Token 1',14,function=None),
            buttons.Buttons(600, 150, 100, 50, screen, agreen, pgreen, 'Token 2',14,function=None),
            buttons.Buttons(600, 250, 100, 50, screen, agreen, pgreen, 'Token 3',14,function=None),
            buttons.Buttons(600, 350, 100, 50, screen, agreen, pgreen, 'Token 4',14,function=None)]

pcylw = [buttons.Buttons(600, 50, 100, 50, screen, ayellow, pyellow, 'Token 1',14,function=None),
            buttons.Buttons(600, 150, 100, 50, screen, ayellow, pyellow, 'Token 2',14,function=None),
            buttons.Buttons(600, 250, 100, 50, screen, ayellow, pyellow, 'Token 3',14,function=None),
            buttons.Buttons(600, 350, 100, 50, screen, ayellow, pyellow, 'Token 4',14,function=None)]

pcble= [buttons.Buttons(600, 50, 100, 50, screen, ablue, pblue, 'Token 1',14,function=None),
            buttons.Buttons(600, 150, 100, 50, screen, ablue, pblue, 'Token 2',14,function=None),
            buttons.Buttons(600, 250, 100, 50, screen, ablue, pblue, 'Token 3',14,function=None),
            buttons.Buttons(600, 350, 100, 50, screen, ablue, pblue, 'Token 4',14,function=None)]

# pcskip= buttons.Buttons(600, 50, 100, 50, screen, acolor, pcolor, 'skip moves',14,function=None)

diceimg = {1: pygame.image.load('resources\dice1.png'),
                 2: pygame.image.load('resources\dice2.png'),
                 3: pygame.image.load('resources\dice3.png'),
                 4: pygame.image.load('resources\dice4.png'),
                 5: pygame.image.load('resources\dice5.png'),
                 6: pygame.image.load('resources\dice6.png')}
###

###Token initiation
Player = {
    0: (player.player(green, screen, '1'), player.player(green, screen, '2'), player.player(green, screen, '3'), player.player(green, screen, '4')),
    1: (player.player(yellow, screen, '1'), player.player(yellow, screen, '2'), player.player(yellow, screen, '3'), player.player(yellow, screen, '4') ),
    2: (player.player(blue, screen, '1'), player.player(blue, screen, '2'), player.player(blue, screen, '3'), player.player(blue, screen, '4')),
    3: (player.player(red, screen, '1'), player.player(red, screen, '2'), player.player(red, screen, '3'), player.player(red, screen, '4'))
}
##

### Start game parameters
sts    = 0
draw = 0
turn  = 0
position = {
    0: [-1, -1, -1, -1],
    1: [-1, -1, -1, -1],
    2: [-1, -1, -1, -1],
    3: [-1, -1, -1, -1]
}
playerturn = 0
firstdraw = [ True, True, True, True]
tokenclick  = True
diceclick = False
###

###button function##
def newgame():
     global  sts
     sts = 1

def exit():
    pygame.quit()
    sys.exit()

# Tambahkan fungsi back_function untuk mengubah nilai sts menjadi 0
# Tambahkan fungsi back_function untuk mengubah nilai sts menjadi 0
def back_function():
    global sts
    sts = 0

# Tambahkan fungsi back_function untuk mengubah nilai sts menjadi 0

# Tambahkan fungsi untuk menampilkan halaman peraturan permainan
# def rules_function():
#     pygame.init()

#     rules_screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption('LUDO GAME')
#     rules_screen.fill((255, 255, 255))
    

#     rule_text = [
#         "Peraturan Permainan Ludo",
#         "",
#         "Persiapan Permainan:",
#         "- Papan permainan Ludo memiliki jalur yang terbagi menjadi empat warna: merah, kuning, hijau, dan biru.",
#         "- Setiap pemain memiliki empat buah pion dalam warna yang sesuai.",
#         "- Pions ditempatkan di rumah masing-masing pemain di ujung jalur.",
#         "",
#         "Tujuan Permainan:",
#         "- Pemain pertama yang berhasil membawa keempat pionnya ke pusat papan permainan adalah pemenangnya.",
#         "",
#         "Aturan Pergeseran Pion:",
#         "- Pion dapat bergerak sejauh jumlah mata dadu yang dilempar.",
#         "- Jika dadu menunjukkan enam, pemain dapat melempar lagi dan bergerak pion baru atau memindahkan pion yang sudah bergerak.",
#         "- Pion hanya dapat diakses oleh pemain yang memiliki warna yang sesuai dengan warna jalur yang diikuti.",
#         "",
#         "Aturan Keamanan (Safe Zone):",
#         "- Kotak yang ditempati oleh pion sendiri adalah zona aman. Pion di zona aman tidak dapat dihentikan oleh pemain lain.",
#         "- Pemain lain tidak dapat melewati zona aman pemain lainnya.",
#         "",
#         "Aturan Memakan Pion Pemain Lain:",
#         "- Jika pion mendarat di kotak yang sudah ditempati oleh pion pemain lain, pion pemain lain tersebut dipindahkan kembali ke rumahnya.",
#         "",
#         "Aturan Masuk ke Pusat:",
#         "- Untuk memasukkan pion ke pusat papan, pemain harus melempar dadu dan mendapatkan jumlah mata yang sesuai dengan jarak yang tersisa menuju pusat.",
#         "- Pemain harus melempar jumlah mata yang pas untuk menyelesaikan perjalanan ke pusat.",
#         "",
#         "Aturan Dadu:",
#         "- Dadu dilempar dengan menekan tombol 'Throw Dice'.",
#         "- Jika dadu jatuh di luar papan atau tidak jelas, pemain harus melempar ulang.",
#         "",
#         "Pemenang:",
#         "- Pemain yang pertama kali membawa keempat pionnya ke pusat papan adalah pemenangnya."
#     ]

#     fontobj = pygame.font.Font('freesansbold.ttf', 20)
#     max_width = 700  # Set the maximum width for text
#     line_height = 25
#     y_position = 50
#     scroll_speed = 10  # Set the scroll speed

#     scroll_y = 0

#     back_btn_rules = buttons.Buttons(350, 550, 100, 50, rules_screen, (255, 0, 0), (200, 0, 0), 'Back', 16, back_function)

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     scroll_y += scroll_speed
#                 elif event.key == pygame.K_DOWN:
#                     scroll_y -= scroll_speed
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 4:  # Mouse wheel scroll up
#                     scroll_y += scroll_speed
#                 elif event.button == 5:  # Mouse wheel scroll down
#                     scroll_y -= scroll_speed
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if back_btn_rules.rect.collidepoint(pygame.mouse.get_pos()):
#                         waiting = False
#                         return

#         rules_screen.fill((255, 255, 255))

#         for line in rule_text:
#             words = line.split(' ')
#             lines = ['']
#             current_line = 0

#             for word in words:
#                 if fontobj.size(lines[current_line] + word)[0] <= max_width:
#                     lines[current_line] += word + ' '
#                 else:
#                     current_line += 1
#                     lines.append(word + ' ')

#             for formatted_line in lines:
#                 display_font = fontobj.render(formatted_line.rstrip(), True, [0, 0, 0])
#                 display_rect = display_font.get_rect(topleft=(50, y_position))
#                 rules_screen.blit(display_font, display_rect)
#                 y_position += line_height

#         # Adjust y_position based on scrolling
#         y_position = 50 - scroll_y

#         back_btn_rules.Draw()

#         pygame.display.flip()


def rules_function():
    pygame.init()

    rules_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('LUDO GAME')
    rules_screen.fill((255, 255, 255))

    title_font = pygame.font.Font('freesansbold.ttf', 32)
    title_text = title_font.render("Peraturan Permainan Ludo", True, [0, 0, 0])
    title_rect = title_text.get_rect(center=(400, 40))

    rule_text = [
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
        "- Pemain yang pertama kali membawa keempat pionnya ke pusat papan adalah pemenangnya."
    ]

    fontobj = pygame.font.Font('freesansbold.ttf', 20)
    max_width = 700  # Set the maximum width for text
    line_height = 25
    y_position = 100
    scroll_speed = 10  # Set the scroll speed

    scroll_y = 0

    back_btn_rules = buttons.Buttons(350, 550, 100, 50, rules_screen, (255, 0, 0), (200, 0, 0), 'Back', 16, back_function)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if scroll_y > -((len(rule_text) * line_height) - 550):
                        scroll_y -= scroll_speed
                elif event.key == pygame.K_DOWN:
                    if scroll_y < 0:
                        scroll_y += scroll_speed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel scroll up
                    if scroll_y > -((len(rule_text) * line_height) - 550):
                        scroll_y -= scroll_speed
                elif event.button == 5:  # Mouse wheel scroll down
                    if scroll_y < 0:
                        scroll_y += scroll_speed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_btn_rules.rect.collidepoint(pygame.mouse.get_pos()):
                        waiting = False
                        return

        rules_screen.fill((255, 255, 255))

        # Draw the title "Peraturan Permainan Ludo" with scrolling
        rules_screen.blit(title_text, (400 - title_rect.width // 2, 40 + scroll_y))

        for line in rule_text:
            display_font = fontobj.render(line, True, (0, 0, 0))
            display_rect = display_font.get_rect(topleft=(50, y_position))
            rules_screen.blit(display_font, display_rect)
            y_position += line_height

        # Adjust y_position based on scrolling
        y_position = 100 - scroll_y

        back_btn_rules.Draw()

        pygame.display.flip()



def about_function():
    pygame.init()

    about_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('LUDO GAME')

    title_font = pygame.font.Font('freesansbold.ttf', 32)
    title_text = title_font.render("About Us", True, [0, 0, 0])
    title_rect = title_text.get_rect(center=(400, 40))

    developer_profiles = [
        {"nama": "Alvalen Shafelbilyunazra", "nim": "220535608548", "photo": "Foto_Almet_Alvalen.png", "offering": "TI - A"},
        {"nama": "Ardha A. P. Agustavada", "nim": "220535608503", "photo": "Foto_Almet_Ardha.png", "offering": "TI - A"},
        {"nama": "Azarya A. K. Moeljono", "nim": "220535608951", "photo": "Azarya_Foto_Almet.png", "offering": "TI - A"},
        # Tambahkan profil pengembang lainnya sesuai kebutuhan
    ]

    fontobj = pygame.font.Font('freesansbold.ttf', 20)
    line_height = 30
    y_position = 100

    max_height = 450
    scroll_speed = 10
    scroll_y = 0

    back_btn_about = buttons.Buttons(350, 550, 100, 50, about_screen, (255, 0, 0), (200, 0, 0), 'Back', 16, back_function)

    description_text = (
        "LudoPy adalah game ludo digital yang dibuat dengan menggunakan bahasa pemrograman python yang didukung oleh open gl, dan py game. Terinspirasi dari ludo konvensional, LudoPy dikembangkan agar menjadi lebih interaktif dan menarik. Berbeda dengan game ludo pada umumnya, LudoPy memiliki fitur unik yaitu random zone dimana ketika pion berada dalam petak atau zone tersebut, maka pion akan berpindah tempat secara acak."
    )

    lorem_font = pygame.font.Font('freesansbold.ttf', 16)
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
            photo_path = os.path.join('resources', profile["photo"])
            developer_image = pygame.image.load(photo_path)
            developer_image = pygame.transform.scale(developer_image, (85, 85))
            about_screen.blit(developer_image, (100, y_position + scroll_y))

            text_lines = [f"{key.capitalize()} : {value}" for key, value in profile.items() if key not in ["photo", "offering"]]
            for line in text_lines:
                display_font = fontobj.render(line, True, [0, 0, 0])
                display_rect = display_font.get_rect(topleft=(200, y_position + scroll_y))
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
    global sts, position ,playerturn, tokenclick, diceclick, firstdraw, draw
    draw = 0
    sts = 0
    position = {
        0: [-1, -1, -1, -1],
        1: [-1, -1, -1, -1],
        2: [-1, -1, -1, -1],
        3: [-1, -1, -1, -1]
    }
    playerturn = 0
    tokenclick = True
    diceclick = False
    firstdraw = [True, True, True, True]

def Throw():
    global draw, tokenclick, diceclick
    if tokenclick == True:
        # draw = random.randint(1, 6)
        draw = random.randint(5, 6)
        tokenclick = False
        diceclick = True
###

###button object###
# Ubah urutan tombol agar sesuai dengan keinginan
newbtn = buttons.Buttons(350, 250, 100, 50, screen, agreen, pgreen, 'New Game', 16, newgame)
rules_btn = buttons.Buttons(350, 330, 100, 50, screen, acolor, pcolor, 'Rules', 16, rules_function)
about_btn = buttons.Buttons(350, 410, 100, 50, screen, ablue, pblue, 'About', 16, about_function)
exitbtn = buttons.Buttons(350, 490, 100, 50, screen, ared, pred, 'Exit', 16, exit)
quitbtn = buttons.Buttons(400, 10, 100, 30, screen, acolor, pcolor, 'Quit Game', 14, quitgame)
quitbtn1 = buttons.Buttons(350, 450, 100, 50, screen, acolor, pcolor, 'Quit Game', 14, quitgame)
dicebtn = buttons.Buttons(100, 10, 100, 30, screen, acolor, pcolor, 'Throw Dice', 14, Throw)
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
                    Player[0][j].draw(GreenPath[position[i][j]][0], GreenPath[position[i][j]][1])
                if i == 1:
                    Player[1][j].draw(YellowPath[position[i][j]][0], YellowPath[position[i][j]][1])
                if i == 2:
                    Player[2][j].draw(BluePath[position[i][j]][0], BluePath[position[i][j]][1])
                if i == 3:
                    Player[3][j].draw(RedPath[position[i][j]][0], RedPath[position[i][j]][1])

def pcd(player):
    pygame.draw.rect(screen, white, pygame.Rect(600, 450, 100, 50))
    fontobj = pygame.font.Font('freesansbold.ttf', 18)
    if player == 0:
        displayfont = fontobj.render('Player 1', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 1:
        displayfont = fontobj.render('Player 2', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 2:
        displayfont = fontobj.render('Player 3', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

    elif player == 3:
        displayfont = fontobj.render('Player 4', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (650, 475)
        screen.blit(displayfont, disrect)

def PlayerTokenSelect(player):
    global playerturn, draw
    if player == 0:
        if draw == 6:
            for i in range(4):
                pcgrn[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcgrn[i].Draw()
        pcd(player)
    if player == 1:
        if draw == 6:
            for i in range(4):
                pcylw[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcylw[i].Draw()
        pcd(player)
    if player == 2:
        if draw == 6:
            for i in range(4):
                pcble[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcble[i].Draw()
        pcd(player)
    if player == 3:
        if draw == 6:
            for i in range(4):
                pcrd[i].Draw()
        else:
            for i in range(4):
                if position[player][i] != -1:
                    pcrd[i].Draw()
        pcd(player)

def CollisionChecker(pt, token):
    global position
    if pt == 0 and position[pt][token]  != -1:
        if position[pt][token] != 8 and position[pt][token] != 21 and position[pt][token] != 34 and position[pt][token] != 47:
            for i in range(4):
                if GreenPath.get(position[pt][token]) == YellowPath.get(position[1][i]):
                    position[1][i] = -1
                if GreenPath.get(position[pt][token]) == BluePath.get(position[2][i]):
                    position[2][i] = -1
                if GreenPath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 1 and position[pt][token]  != -1:
        if position[pt][token] != 8 and position[pt][token] != 21 and position[pt][token] != 34 and position[pt][token] != 47:
            for i in range(4):
                if YellowPath.get(position[pt][token]) == GreenPath.get(position[0][i]):
                    position[0][i] = -1
                if YellowPath.get(position[pt][token]) == BluePath.get(position[2][i]):
                    position[2][i] = -1
                if YellowPath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 2 and position[pt][token]  != -1:
        if position[pt][token] != 8 and position[pt][token] != 21 and position[pt][token] != 34 and position[pt][token] != 47:
            for i in range(4):
                if BluePath.get(position[pt][token]) == GreenPath.get(position[0][i]):
                    position[0][i] = -1
                if BluePath.get(position[pt][token]) == YellowPath.get(position[1][i]):
                    position[1][i] = -1
                if BluePath.get(position[pt][token]) == RedPath.get(position[3][i]):
                    position[3][i] = -1
    elif pt == 3 and position[pt][token]  != -1:
        if position[pt][token] != 8 and position[pt][token] != 21 and position[pt][token] != 34 and position[pt][token] != 47:
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
        if 700 >= pos()[0] >=600 and 100 >= pos()[1] >= 50:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][0] += 1
                        firstdraw[playerturn] = False
                        diceclick = True
                        playerturn = -1
                    
                elif position[playerturn][0] + draw < 57:
                    if draw == 6:
                        position[playerturn][0] += 6
                        diceclick = True
                        playerturn = -1
                    else:
                        position[playerturn][0] += draw
                CollisionChecker(playerturn, 0)
                diceclick = False
                tokenclick = True
                playerturn += 1

        if 700 >= pos()[0] >=600 and 200 >= pos()[1] >= 150:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][1] += 1
                        firstdraw[playerturn] = False
                        diceclick = True
                        playerturn = 0
                        
                elif position[playerturn][1] + draw < 57:
                    if draw == 6:
                        position[playerturn][1] += 6
                        diceclick = True
                        playerturn = 0
                    else:
                        position[playerturn][1] += draw
                CollisionChecker(playerturn, 1)
                diceclick = False
                tokenclick = True
                playerturn += 1

        if 700 >= pos()[0] >= 600 and 300 >= pos()[1] >= 250:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][2] += 1
                        firstdraw[playerturn] = False
                        diceclick = True
                        playerturn = 1

                elif position[playerturn][2] + draw < 57:
                    if draw == 6:
                        position[playerturn][2] += 6
                        diceclick = True
                        playerturn = 1
                    else:
                        position[playerturn][2] += draw
                CollisionChecker(playerturn, 2)
                diceclick = False
                tokenclick = True
                playerturn += 1

        if 700 >= pos()[0] >=600 and 400 >= pos()[1] >= 350:
            if pygame.mouse.get_pressed()[0] == 1:
                if firstdraw[playerturn] == True:
                    if draw == 6:
                        position[playerturn][3] += 1
                        firstdraw[playerturn] = False
                        diceclick = True
                        playerturn = 2

                elif position[playerturn][3] + draw < 57:
                    if draw == 6:
                        position[playerturn][3] += 6
                        diceclick = True
                        playerturn = 2
                    else:
                        position[playerturn][3] += draw
                CollisionChecker(playerturn, 3)
                diceclick = False
                tokenclick = True
                playerturn += 1

def win():
    if position[0][0] == 56 and position[0][1] == 56 and position[0][2] == 56 and position[0][3] == 56:
        return True
    elif position[1][0] == 56 and position[1][1] == 56 and position[1][2] == 56 and position[1][3] == 56:
        return True
    elif position[2][0] == 56 and position[2][1] == 56 and position[2][2] == 56 and position[2][3] == 56:
        return True
    elif position[3][0] == 56 and position[3][1] == 56 and position[3][2] == 56 and position[3][3] == 56:
        return True
    return False

def showwin(ply):
    fontobj = pygame.font.Font('freesansbold.ttf', 35)
    screen.fill((255, 255, 255))
    if ply == 4:
        ply = 0
    if ply == 0:
        displayfont = fontobj.render('player green won', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 1:
        displayfont = fontobj.render('Player Yellow won', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 2:
        displayfont = fontobj.render('Player Blue won', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)

    elif ply == 3:
        displayfont = fontobj.render('Player Red won', True, [0, 0, 0])
        disrect = displayfont.get_rect()
        disrect.center = (400, 300)
        screen.blit(displayfont, disrect)
    quitbtn1.Draw()
sex=0

###Actual Loop
while True:
    pygame.display.flip()
    if sts == 0:
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
            if sex == 57: sex=0
            Player[0][1].draw(GreenPath[sex][0], GreenPath[sex][1])
            Player[1][1].draw(YellowPath[sex][0], YellowPath[sex][1])
            Player[2][1].draw(BluePath[sex][0], BluePath[sex][1])
            Player[3][1].draw(RedPath[sex][0], RedPath[sex][1])

            sex +=1
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