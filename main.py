import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the cube vertices and edges
vertices = (
    (1, -1, -1), (1, 1, -1),
    (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1),
    (-1, -1, 1), (-1, 1, 1)
)

edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
)

# Function to create a cube
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main display function
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_caption("05 Performance Task 1, Dela Pena_Jay Daniel_701")
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -25)

    # Define cube colors
    colors = [
        (1, 0, 0),  # Red
        (0, 1, 0),  # Green
        (0, 0, 1),  # Blue
        (1, 0.5, 0), # Orange
        (0.5, 0, 0.5) # Purple
    ]

    x_move = y_move = 0
    rotate = False
    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_move = -0.1
                elif event.key == pygame.K_s:
                    y_move = 0.1
                elif event.key == pygame.K_a:
                    x_move = -0.1
                elif event.key == pygame.K_d:
                    x_move = 0.1
                elif event.key == pygame.K_r:
                    rotate = not rotate

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s]:
                    y_move = 0
                elif event.key in [pygame.K_a, pygame.K_d]:
                    x_move = 0

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Translate the cubes
        glTranslatef(x_move, y_move, 0)

        # Rotate the cubes if 'R' is pressed
        if rotate:
            rotation_angle += 1
        glRotatef(rotation_angle, 0, 0, 1)

        # Draw the cubes
        for i, color in enumerate(colors):
            glColor3fv(color)
            glPushMatrix()
            glTranslatef(i * 4 - 8, 0, 0)  # Position each cube
            if i >= 3:  # Rotate last two cubes initially
                glRotatef(45, 0, 0, 1)
            Cube()
            glPopMatrix()

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

main()
