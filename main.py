# -*- coding: utf-8 -*-

import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


import cartpole
import controller


class Main:
    def __init__(self):
        self.robo = cartpole.cart_pole()
        self.ctrl = controller.Controller()
        self.learn_epoch_max = 10
        self.epoch = 0
        self.timeMax = 200
        self.time = 0
        
    def learn(self):
        self.epoch = 0
        self.time = 0
        
        #single epoch
        while(True):
            print("learning..",self.epoch)
            
            self.epoch += 1
            
            #single learn
            while(True):
                self.time += 1
                self.robo.simulateSingleStep()
                
                if(self.time > self.timeMax):
                    self.robo.reset()
                    self.time = 0
                    break
                
            if(self.epoch > self.learn_epoch_max):
                break
            
    
    def animation(self,value):
    
        u = self.ctrl.getOutput()
        self.robo.addForce(u)
        
        self.robo.simulateSingleStep()

        glutPostRedisplay()
    
        self.time += 1
        if(self.time > self.timeMax):
            self.robo.reset()
            self.time = 0
            self.learn()

        glutTimerFunc(self.robo.stepTime, self.animation, 0)

    def display(self):
    
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
            
        self.robo.draw()
        
        glFlush()  # enforce OpenGL command

    def resize(self,w, h):
        glViewport(0, 0, w, h);
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(-w / 200.0, w / 200.0, -h / 200.0, h / 200.0, -1.0, 1.0);
        
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        


#main
    def main(self):
        width = 400
        height = 300
        
        glutInitWindowSize(width, height)     # window size
        glutInitWindowPosition(100, 100) # window position
        
        glutInit(sys.argv)
    
        glutInitDisplayMode(GLUT_RGBA)

        glutCreateWindow(b"cartPole")      # show window
    
        glutDisplayFunc(self.display)         # draw callback function
        
        glutReshapeFunc(self.resize);
    
        """ initialize """
        glClearColor(1.0, 1.0, 1.0, 1.0)
    
        #start timer
        glutTimerFunc(self.robo.stepTime, self.animation, 0);
        
        glutMainLoop()


if __name__ == "__main__":
    m = Main()
    m.main()