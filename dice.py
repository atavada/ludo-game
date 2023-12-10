import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image  # Updated import for Python 3
import time
import numpy as np

# string to identify when ESC is pressed
ESCAPE = "\033"
RETURN = "\r"

# ID of the Pygame window
window = 0
dice = 0
# angle and rotation coordinates of the cube
angulo = 0.0
xrot = yrot = zrot = 5.0
texCounter = 0
start_time = 0
spinning = True

# cube vertices
vertices = (
    (1, -1, -1),  # 0
    (1, 1, -1),  # 1
    (-1, 1, -1),  # 2
    (-1, -1, -1),  # 3
    (1, -1, 1),  # 4
    (1, 1, 1),  # 5
    (-1, -1, 1),  # 6
    (-1, 1, 1),  # 7
)

# different colors for each surface
cores = (
    (0.0, 1.0, 0.0),
    (1.0, 0.5, 0.0),
    (1.0, 0.0, 0.0),
    (1.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
    (1.0, 0.0, 1.0),
)

# surfaces of the cube with four points
superficies = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

texSuperficies = (
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (3, 0, 1, 2),
    (2, 3, 0, 1),
    (1, 2, 3, 0),
    (0, 1, 2, 3),
)

texturas = ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
image_filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]
image = []
loaded = {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
}
for filename in image_filenames:
    img = Image.open("textures-fast/" + filename)
    img = img.convert("RGB")
    image.append(img)

textures = []


def LoadTextures():
    global image, textures

    for img in image:
        ix, iy = img.size
        strImage = img.tobytes("raw", "RGB", 0, -1)  # Updated method to get image bytes

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, strImage)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        textures.append(texture)

# called immediately after creating the window
def InitGL(width, height):
    # load textures
    glEnable(GL_TEXTURE_2D)
    LoadTextures()

    # clear the background with black color
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # clear Depth Buffer
    glClearDepth(1.0)
    # Type of depth test to be performed
    glDepthFunc(GL_LESS)
    # enable depth test
    glEnable(GL_DEPTH_TEST)
    # enable Smooth Color Shading
    glShadeModel(GL_SMOOTH)
    # add lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1))

    

    # Perspective calculations
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def CleanupGL():
    glFlush()
    glDisable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_DONT_CARE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    textures_array = np.array(textures, dtype=np.uint32)
    glDeleteTextures(textures_array)

    global xrot, yrot, zrot
    xrot = yrot = zrot = 0.0


# Redraw window when it is resized
def ReSizeGLScene(width, height):
    # prevent size from being zero
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# Draw objects in the environment
def DrawGLScene(dice):
    global xrot, yrot, zrot, spinning, start_time, window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # coords of the cube
    coords = {
        1: [176, 0, 0],
        2: [0, 88, 0],
        3: [0, 0, 0],
        4: [0, 270, 0],
        5: [88, 0, 0],
        6: [270, 0, 0],
    }
    glTranslatef(0.0, 0.0, -10)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    # Drawing area
    for i, superficie in enumerate(superficies):
        glBindTexture(GL_TEXTURE_2D, textures[i])
        glBegin(GL_QUADS)
        texVertices = texSuperficies[i]
        for i, vertice in enumerate(superficie):
            glTexCoord2fv(texturas[texVertices[i]])
            glVertex3fv(vertices[vertice])
        glEnd()

    pygame.display.flip()

    if spinning:
        elapsed_time = time.time() - start_time

        if elapsed_time < 1:
            # Random rotation
            xrot += 1
            yrot += 1
            zrot += 1
        else:
            # Use coords and number to determine the rotation
            number = dice
            if xrot < coords[number][0]:
                xrot += 1
            elif xrot > coords[number][0]:
                xrot -= 1
            if yrot < coords[number][1]:
                yrot += 1
            elif yrot > coords[number][1]:
                yrot -= 1
            if zrot < coords[number][2]:
                zrot += 1
            elif zrot > coords[number][2]:
                zrot -= 1
            if (
                xrot == coords[number][0]
                and yrot == coords[number][1]
                and zrot == coords[number][2]
            ):
                spinning = False
                pygame.time.wait(1000)


def start(dice):
    global window, spinning, start_time
    spinning = True
    start_time = time.time()

    pygame.init()
    display = (800, 600)
    window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    InitGL(800, 600)
    while spinning:
        DrawGLScene(dice)


if __name__ == "__main__":
    start()
