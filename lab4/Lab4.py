import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

cube_vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
cube_edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

tetra_vertices = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
tetra_edges = ((0,1), (0,2), (0,3), (1,2), (1,3), (2,3))

colors = ((1,0,0),(0,1,0),(0,0,1),(0,1,0),(1,1,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1),(1,0,0),(1,1,1),(0,1,1))

color_index = 0
rotate = True
speed = 1
shape = "cube"
fill = False

def Cube():
    glBegin(GL_POLYGON if fill else GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            glColor3fv(colors[color_index])
            glVertex3fv(cube_vertices[vertex])
    glEnd()

def Tetrahedron():
    glBegin(GL_POLYGON if fill else GL_LINES)
    for edge in tetra_edges:
        for vertex in edge:
            glColor3fv(colors[color_index])
            glVertex3fv(tetra_vertices[vertex])
    glEnd()

def main():
    global color_index, rotate, speed, shape, fill
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    color_index = (color_index + 1) % len(colors)
                elif event.button == 3:  # Right mouse button.
                    rotate = not rotate
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed += 1
                elif event.key == pygame.K_DOWN:
                    speed -= 1
                elif event.key == pygame.K_SPACE:
                    shape = "cube" if shape == "tetra" else "tetra"
                elif event.key == pygame.K_l:
                    fill = not fill

        if rotate:
            glRotatef(speed, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if shape == "cube":
            Cube()
        else:
            Tetrahedron()
        pygame.display.flip()
        pygame.time.wait(10)

main()
