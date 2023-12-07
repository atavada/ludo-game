from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image  # Updated import for Python 3
import sys
import random as r
import time

# string to identify when ESC is pressed
ESCAPE = "\033"
RETURN = "\r"

# ID of the GLUT window
window = 0

# angle and rotation coordinates of the cube
angulo = 0.0
xrot = yrot = zrot = 5.0
texCounter = 0

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
image = []


# load textures from the saved images in the array
def LoadTextures(index):
    global image

    ix, iy = image[index].size
    strImage = image[index].tobytes(
        "raw", "RGBX", 0, -1
    )  # Updated method to get image bytes

    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, strImage)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


# Configure initial parameters of the window
# called immediately after creating the window
def InitGL(width, height):
    # load textures
    LoadTextures(0)
    glEnable(GL_TEXTURE_2D)

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

    # Perspective calculations
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


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


# Increase rotation speed when the key is pressed
# def increaseRotation():
#     global angulo, xrot, yrot, zrot
#     # ... (unchanged)

# Decrease rotation speed to show the obtained number
# def decreaseRotation():
#     global angulo, xrot, yrot, zrot
#     # ... (unchanged)


# Draw objects in the environment
def DrawGLScene():
    global angulo, xrot, yrot, zrot, texCounter
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -10)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    # Drawing area
    for i, superficie in enumerate(superficies):
        LoadTextures(i)
        glBegin(GL_QUADS)
        texVertices = texSuperficies[i]
        for i, vertice in enumerate(superficie):
            glTexCoord2fv(texturas[texVertices[i]])
            glVertex3fv(vertices[vertice])
        glEnd()

    glutSwapBuffers()

    xrot += 1.0
    yrot += 1.0
    zrot += 1.0


# Manage pressed keys
def keyPressed(*args):
    global angulo, xrot, yrot, zrot
    global window

    # ESCAPE
    if args[0] == ESCAPE:
        sys.exit()
    if args[0] == RETURN:
        print("Launching process to be implemented")


def main(*args):
    global window, image

    # check command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "fast" or sys.argv[1] == "slow":
            for i in range(1, 7):
                image.append(
                    Image.open("textures-" + sys.argv[1] + "/" + str(i) + ".jpg")
                )
        else:
            print("dice.py: invalid option", sys.argv[1])
            print("Default texture mode applied.")
            for i in range(1, 7):
                image.append(Image.open("textures-fast/" + str(i) + ".jpg"))
    else:
        for i in range(1, 7):
            image.append(Image.open("textures-fast/" + str(i) + ".jpg"))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("3D Dice")

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)

    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
