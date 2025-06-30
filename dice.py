"""
Alejandro Vega
"""

import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np


def normals(v1,v2,v3):
    edge1 = np.subtract(v2,v1)
    edge2 = np.subtract(v3,v1)
    normal = np.cross(edge1,edge2)
    normal = normal / np.linalg.norm(normal)
    return normal


def Tetra():
    VERTICES = (
        (1, 1, -1), (-1, -1, -1), (1, -1, 1), (-1, 1, 1)
        )

    EDGES = (
        (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
        )
    
    SURFACES = (
        (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)
        )
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))
    
    NORMALS = []
    
    texture_coords = [
        
        [((0/700),0), ((50/700),1), ((100/700),0)], #1
        [((100/700),0), ((200/700),0), ((150/700),1)], #2
        [((200/700),0), ((300/700),0), ((250/700),1)], #3
        [((300/700),0), ((400/700),0), ((350/700),1)] #4
        
        ]
    
    for surface in SURFACES:
        v0 = VERTICES[surface[0]]
        v1 = VERTICES[surface[1]]
        v2 = VERTICES[surface[2]]
        NORMALS.append(normals(v0,v1,v2))
    
    
    for surface_index, surface in enumerate(SURFACES):
        glBegin(GL_TRIANGLES)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index, vertex in enumerate(surface):
            index = (surface_index + vertex_index) % 2
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(VERTICES[vertex])
            
        glEnd()
    
    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(VERTICES[vertex])
    glEnd()
      

def Cube():
    VERTICES = (
        ( 1, -1, -1), # 0
        ( 1,  1, -1), # 1
        (-1,  1, -1), # 2
        (-1, -1, -1), # 3
        ( 1, -1,  1), # 4
        ( 1,  1,  1), # 5
        (-1, -1,  1), # 6
        (-1,  1,  1), # 7
        )

    SURFACES = ((0,1,2,3), (3,2,7,6), (6,7,5,4), (4,5,1,0), (1,5,7,2), (4,0,3,6))

    NORMALS = [
        ( 0,  0, -1),  # surface 0
        (-1,  0,  0),  # surface 1
        ( 0,  0,  1),  # surface 2
        ( 1,  0,  0),  # surface 3
        ( 0,  1,  0),  # surface 4
        ( 0, -1,  0)   # surface 5
    ]

    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))

    EDGES = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

    texture_coords = [
        
        [((0/700),0), ((0/700),1), ((100/700),1), ((100/700),0)], #1
        [((200/700),0), ((200/700),1), ((300/700),1), ((300/700),0)], #3
        [((500/700),0), ((500/700),1), ((600/700),1), ((600/700),0)], #6
        [((300/700),0), ((300/700),1), ((400/700),1), ((400/700),0)], #4
        [((100/700),0), ((100/700),1), ((200/700),1), ((200/700),0)], #2
        [((400/700),0), ((400/700),1), ((500/700),1), ((500/700),0)] #5
        
        ]
    
    for surface_index, surface in enumerate(SURFACES):
        glBegin(GL_QUADS)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index, vertex in enumerate(surface):
            index = (surface_index + vertex_index) % 2
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(VERTICES[vertex])
            
        glEnd()
    
    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(VERTICES[vertex])
    glEnd()
    

def Octo():
    VERTICES = (
        (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0),
        (0, 0, 1), (0, 0, -1)
        )

    EDGES = (
        (0,1), (0,3), (0,4), (0,5), (1,2), (1,4), (1,5), (2,3),
        (2,4), (2,5), (3,4), (3,5)
        )
    
    SURFACES = (
        (0, 1, 4),  #1
        (0, 1, 5),  #2
        (0, 3, 4),  #3
        (5, 3, 0),  #4
        (2, 1, 4),  #5
        (5, 1, 2),  #6
        (4, 3, 2),  #7
        (2, 3, 5)   #8
        )
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))
    
    NORMALS = []
    
    texture_coords = [
        
        [((0/900),0), ((50/900),1), ((100/900),0)], #1
        [((100/900),0), ((200/900),0), ((150/900),1)], #2
        [((200/900),0), ((300/900),0), ((250/900),1)], #3
        [((300/900),0), ((400/900),0), ((350/900),1)], #4
        [((400/900),0), ((500/900),0), ((450/900),1)], #5
        [((500/900),0), ((600/900),0), ((550/900),1)], #6
        [((600/900),0), ((700/900),0), ((650/900),1)], #7
        [((700/900),0), ((800/900),0), ((750/900),1)], #8
        
        ]
    
    for surface in SURFACES:
        v0 = VERTICES[surface[0]]
        v1 = VERTICES[surface[1]]
        v2 = VERTICES[surface[2]]
        NORMALS.append(normals(v0,v1,v2))
    
    
    for surface_index, surface in enumerate(SURFACES):
        glBegin(GL_TRIANGLES)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index, vertex in enumerate(surface):
            index = (surface_index + vertex_index) % 2
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(VERTICES[vertex])
            
        glEnd()
    
    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(VERTICES[vertex])
    glEnd()


def Dodeca():
    phi = (1 + math.sqrt(5))/2
    k = 1/math.sqrt(3)
    VERTICES = (
        (k, k, k), (-k, k, k),
        (k, -k, k), (-k, -k, k),
        (k, k, -k), (-k, k, -k),
        (k, -k, -k), (-k,-k,-k),
        (0, k/phi, k*phi), (0, k/phi, -k*phi),
        (0, -k/phi, k*phi), (0, -k/phi, -k*phi),
        (k/phi, k*phi, 0), (k/phi, -k*phi, 0),
        (-k/phi, k*phi, 0), (-k/phi, -k*phi, 0),
        (k*phi, 0, k/phi), (k*phi, 0, -k/phi),
        (-k*phi, 0, k/phi), (-k*phi, 0, -k/phi)
        )

    EDGES = (
       (0, 8), (0, 12), (0, 16), (1, 8), (1, 14), (1, 18), 
       (2, 10), (2, 13), (2, 16), (3, 10), (3, 15), (3, 18), 
       (4, 9), (4, 12), (4, 17), (5, 9), (5, 14), (5, 19), 
       (6, 11), (6, 13), (6, 17), (7, 11), (7, 15), (7, 19), 
       (8, 10), (9, 11), (12, 14), (13, 15), (16, 17), (18, 19)
        )

    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1), (1,0,0))
    
    SURFACES = (
        
        (0, 8, 10, 2, 16), #1
        (0, 12, 14, 1, 8), #2
        (0, 16, 17, 4, 12), #3
        (1, 8, 10, 3, 18), #4
        (1, 18, 19, 5, 14), #5
        (3, 15, 7, 19, 18),
        (2, 16, 17, 6, 13), #7
        (7, 11, 6, 13, 15), #8
        (7, 11, 9, 5, 19), #9
        (4, 12, 14, 5, 9), #10
        (4, 9, 11, 6, 17), #11
        (15, 3, 10, 2, 13) #12
        
        )
    
    NORMALS = []
    
    texture_coords = [
        
        [((20/1300),0), ((80/1300),0), ((100/1300),.62), ((50/1300),1), ((0/1300),.62)],
        [((120/1300),0), ((180/1300),0), ((200/1300),.62), ((150/1300),1), ((100/1300),.62)],
        [((220/1300),0), ((280/1300),0), ((300/1300),.62), ((250/1300),1), ((200/1300),.62)],
        [((320/1300),0), ((300/1300),.62), ((350/1300),1), ((400/1300),.62), ((380/1300),0)], 
        [((420/1300),0), ((400/1300),.62), ((450/1300),1), ((500/1300),.62), ((480/1300),0)], 
        [((520/1300),0), ((500/1300),.62), ((550/1300),1), ((600/1300),.62), ((580/1300),0)], 
        [((620/1300),0), ((600/1300),.62), ((650/1300),1), ((700/1300),.62), ((680/1300),0)], 
        [((720/1300),0), ((700/1300),.62), ((750/1300),1), ((800/1300),.62), ((780/1300),0)],
        [((820/1300),0), ((800/1300),.62), ((850/1300),1), ((900/1300),.62), ((880/1300),0)],
        [((920/1300),0), ((900/1300),.62), ((950/1300),1), ((1000/1300),.62), ((980/1300),0)],
        [((1020/1300),0), ((1000/1300),.62), ((1050/1300),1), ((1100/1300),.62), ((1080/1300),0)],
        [((1120/1300),0), ((1100/1300),.62), ((1150/1300),1), ((1200/1300),.62), ((1180/1300),0)]
        
        ]
    
    
    for surface in SURFACES:
        v0 = VERTICES[surface[0]]
        v1 = VERTICES[surface[1]]
        v2 = VERTICES[surface[2]]
        NORMALS.append(normals(v0,v1,v2))
    
    
    for surface_index, surface in enumerate(SURFACES):
        glBegin(GL_POLYGON)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index, vertex in enumerate(surface):
            index = (surface_index + vertex_index) % 2
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(VERTICES[vertex])
            
        glEnd()
    
    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(VERTICES[vertex])
    glEnd()


def Icosa():
    phi = (1 + math.sqrt(5))/2
    k = 1/math.sqrt(1+phi**2)
    VERTICES = (
        (k, 0, phi*k), (-k, 0, phi*k),
        (phi*k, k, 0), (phi*k, -k, 0),
        (0, -phi*k, k), (0, -phi*k, -k), 
        (-phi*k, k, 0), (-phi*k, -k, 0),
        (0, phi*k, k), (0, phi*k, -k),
        (k, 0, -phi*k), (-k, 0, -phi*k)
        )

    EDGES = (
        (0,1), (0,2), (0,3), (0,4), (0,8), (1,4), (1,6), (1,7),
        (1,8), (2,3), (2,8), (2,9), (2,10), (3,4), (3,5), (3,10),
        (4,5), (4,7), (5,7), (5,10), (5,11), (6,7), (6,8), (6,9),
        (6,11), (7,11), (8,9), (9,10), (9,11), (10,11)
        )

    SURFACES = (
        
        (0, 1, 8),  #1
        (8, 2, 0),  #2
        (0, 3, 4),  #3
        (0, 4, 1),  #4
        (0, 2, 3),  #5
        (1, 4, 7),  #6
        (1, 6, 8),  #7
        (11, 6, 9),  #8
        (7, 6, 1),  #9
        (10, 3, 2), #10
        (2, 8, 9),  #11
        (2, 9, 10), #12
        (5, 4, 3),  #13
        (10, 5, 3), #14
        (4, 5, 7),  #15
        (5, 10, 11),#16
        (11, 7, 5), #17
        (9, 8, 6),  #18
        (6, 7, 11), #19
        (11, 10, 9) #20
        
        )
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))
    
    NORMALS = []
    
    texture_coords = [
        
        [((0/2100),0), ((50/2100),1), ((100/2100),0)], #1
        [((100/2100),0), ((150/2100),1), ((200/2100),0)],
        [((200/2100),0), ((250/2100),1), ((300/2100),0)],
        [((300/2100),0), ((350/2100),1), ((400/2100),0)],
        [((400/2100),0), ((450/2100),1), ((500/2100),0)],
        [((500/2100),0), ((550/2100),1), ((600/2100),0)],
        [((600/2100),0), ((650/2100),1), ((700/2100),0)],
        [((700/2100),0), ((750/2100),1), ((800/2100),0)],
        [((800/2100),0), ((850/2100),1), ((900/2100),0)],
        [((900/2100),0), ((950/2100),1), ((1000/2100),0)],
        [((1000/2100),0), ((1050/2100),1), ((1100/2100),0)],
        [((1100/2100),0), ((1150/2100),1), ((1200/2100),0)],
        [((1200/2100),0), ((1250/2100),1), ((1300/2100),0)],
        [((1300/2100),0), ((1350/2100),1), ((1400/2100),0)],
        [((1400/2100),0), ((1450/2100),1), ((1500/2100),0)],
        [((1500/2100),0), ((1550/2100),1), ((1600/2100),0)],
        [((1600/2100),0), ((1650/2100),1), ((1700/2100),0)],
        [((1700/2100),0), ((1750/2100),1), ((1800/2100),0)],
        [((1800/2100),0), ((1850/2100),1), ((1900/2100),0)],
        [((1900/2100),0), ((1950/2100),1), ((2000/2100),0)]
        
        ]
    
    for surface in SURFACES:
        v0 = VERTICES[surface[0]]
        v1 = VERTICES[surface[1]]
        v2 = VERTICES[surface[2]]
        NORMALS.append(normals(v0,v1,v2))
    
    
    for surface_index, surface in enumerate(SURFACES):
        glBegin(GL_TRIANGLES)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index, vertex in enumerate(surface):
            index = (surface_index + vertex_index) % 2
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(VERTICES[vertex])
            
        glEnd()
    
    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(VERTICES[vertex])
    glEnd()


def loadTexture(filename):
    textureSurface = pygame.image.load(filename)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Bonus Assignment')

    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    glLight(GL_LIGHT0, GL_POSITION,  (12, -5, -5, 1))
    
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST) 
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
    
    shape = Tetra
    loadTexture('tetra.png')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        keys = pygame.key.get_pressed()
        
        # pick shape based on keys pressed
        options = {pygame.K_1: (Tetra, 'tetra.png'),
                   pygame.K_2: (Cube, 'cube.png'),
                   pygame.K_3: (Octo, 'octo.png'),
                   pygame.K_4: (Dodeca, 'dodeca.png'),
                   pygame.K_5: (Icosa, 'icosa.png')
                   }
        
        for key, (value, texture) in options.items():
            if keys[key]:
                shape = value
                loadTexture(texture)
                
        
        
        glRotatef(1, 3, 5, 0)
        
        shape()
        
            
        
        pygame.display.flip()
        clock.tick(50)
        
main()