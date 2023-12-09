import pygame  # modul pygame digunakan untuk membuat display
from pygame.locals import *  # modul pygame.locals digunakan untuk mengatur event
from OpenGL.GL import *  # modul OpenGL.GL digunakan untuk menggambar objek
from OpenGL.GLU import *  # modul OpenGL.GLU digunakan untuk membuat perspektif
import pygame.font
import math

menu_state = 0

def draw_button(font_size, text, x, y, width, height, colorText, colorBG):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, colorText, colorBG)
    text_x = int(x + (width - text_surface.get_width()) / 2)
    text_y = int(y + (height - text_surface.get_height()) / 2)
    # Draw the rectangle (background)
    glBegin(GL_QUADS)
    glColor3f(colorBG[0], colorBG[1], colorBG[2])
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    # Draw the centered text
    glPushMatrix()
    glRasterPos2i(text_x, text_y)
    glDrawPixels(
        text_surface.get_width(),
        text_surface.get_height(),
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        pygame.image.tostring(text_surface, "RGBA", True),
    )
    glPopMatrix()


class Button:
    def __init__(self, font, x, y, width, height, text, colorText, colorBG):
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colorText = colorText
        self.colorBG = colorBG

    def draw(self):
        draw_button(
            self.font,
            self.text,
            self.x,
            self.y,
            self.width,
            self.height,
            self.colorText,
            self.colorBG,
        )

    def isClicked(self, x, y):
            # Use mouse position to check if the mouse is clicked
            # Adjust conditions to align with OpenGL's coordinate system
            if (
                x >= self.x
                and x <= self.x + self.width
                and y <= pygame.display.get_surface().get_height() - self.y
                and y >= pygame.display.get_surface().get_height() - (self.y + self.height)
            ) and pygame.mouse.get_pressed()[0] == 1:
                return True
            else:
                return False


def home():
    global menu_state
    # create object button
    start_button = Button(40, 330, 400, 150, 50, "Start", (255, 0, 0), (0, 0, 255))
    start_button.draw()

    about_button = Button(40, 330, 300, 150, 50, "About", (255, 0, 0), (0, 0, 255))
    about_button.draw()
    # check if button is clicked
    if start_button.isClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        menu_state = 1
    elif about_button.isClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        menu_state = 2

def about():
    global menu_state

    # create object button
    back_button = Button(40, 0, 0, 150, 50, "Back", (255, 0, 0), (0, 0, 255))
    back_button.draw()
    # check if button is clicked
    if back_button.isClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        menu_state = 0

        
def game_screen():
    global menu_state



def main():
    h = 800
    w = 800
    pygame.init()  # inisiasi pygame
    pygame.font.init()  # Initialize the font module
    # Create a font object (None for default font, 36 for font size)
    pygame.display.set_caption("OpenGL Coding Practice")  # judul display
    display = (w, h)  # ukuran display
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, w, 0, h)  # set ukuran display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        global menu_state
        if menu_state == 0:
            home()
        elif menu_state == 1:
            game_screen()
        elif menu_state == 2:
            about()
            
            
        pygame.display.flip()
        pygame.time.wait(10)


main()  # memanggil fungsi main
