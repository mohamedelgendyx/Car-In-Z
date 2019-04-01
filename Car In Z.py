from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

angle=1
x=0
forward =True

def road(p):
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glBegin(GL_QUADS)
    glColor3f(.2, .2, .2)
    glVertex(-10, -2.5 * .25, -4*p)
    glVertex(-10, -2.5 * .25, 1.02*p)
    glVertex(120, -2.5 * .25, 1.02*p)
    glVertex(120, -2.5 * .25, - 4*p)
    glEnd()

def sidewalk(k,X,o):
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(X, -2.2 * 0.25, o*-4.3)
    glTranslate(-x*k, 0, 0)
    glScale(1, 0.25, .5)
    glutSolidCube(3)

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,.1,100)
    gluLookAt(8,9,10 ,0,0,0 ,0,1,0)

def wheel(X,Y,Z):
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(X,Y,Z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, .5, 13, 14)

def torch(X,Y,Z):
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1,1,0)
    glTranslate(X,Y,Z)
    glutSolidSphere(0.4,100,100)

def Draw():
    glClearColor(0, .4, 0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global forward
    glMatrixMode(GL_MODELVIEW)

    road(4)
    co = 1

    for i in range(120,-30,-3):
        co*=-1
        glColor3f(co,co,co)
        sidewalk(1,i,1)
        sidewalk(1,i,-1)
        sidewalk(-1,i, 4)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-x, 0, 0)
    glColor3f(1,1,1)
    for i in range(120,-20,-7):
        glBegin(GL_QUADS)
        glVertex(i, -2.5 * .25, -.1)
        glVertex(i, -2.5 * .25, .6)
        glVertex(i+4, -2.5 * .25, .6)
        glVertex(i+4, -2.5 * .25, - .1)
        glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x, 0, 0)
    glTranslate(0, 0,-11)
    glColor3f(1, 1, 1)
    for i in range(100, -50, -7):
        glBegin(GL_QUADS)
        glVertex(i, -2.5 * .25, -.1)
        glVertex(i, -2.5 * .25, .6)
        glVertex(i + 4, -2.5 * .25, .6)
        glVertex(i + 4, -2.5 * .25, - .1)
        glEnd()

    wheel(2.5 + x, -2.5 * 0.25, 2.5 * 0.5)
    wheel(-2.5 + x, -2.5 * 0.25, 2.5 * 0.5)
    wheel(2.5 + x, -2.5 * 0.25, -2.5 * 0.5)
    wheel(-2.5 + x, -2.5 * 0.25, -2.5 * 0.5)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(0, .035, .315)
    glTranslate(x,0,0)
    glScale(1,0.25,.5)
    glutSolidCube(5)

    glLoadIdentity() #matrix of model view Of Translation opertaions
    glRotate(90, 0, 1, 0)
    glColor3f(0,0.152,.356)
    glTranslate(0+x,5*.25,0)
    glScale(.5,0.25,0.5)
    glutSolidCube(5)


    torch(-2.5+x,0,-1.25)
    torch(-2.5+x,0,.5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0, sin(90), 1)
    glTranslate(-2.5*x+63,0,-13)
    glutWireSphere(3, 20, 20)

    if x>27:
        forward=False
    if x<-7:
        forward=True
    if forward:
        x += 0.03
        angle -= 0.3
    else:
        x-=0.03
        angle +=0.3


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Car In Z")
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
myInit()
glutMainLoop()