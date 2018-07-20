import pygame
from pygame.locals import *
import random
# file that contains the class

#class for creating and displaying the map
class Map():

    def __init__(self):
        self.matrix = []
        self.windowSize = 450
        self.nbSprite = 15
        self.spriteSize = self.windowSize / self.nbSprite
        self.window = pygame.display.set_mode([450, 450])
        self.background = pygame.image.load("images/fond.jpg").convert()
        self.wall = pygame.image.load("images/mur2.png").convert()
        self.ether = pygame.image.load("images/ether.png").convert()
        self.needle = pygame.image.load("images/aiguille.png").convert()
        self.tube = pygame.image.load("images/tube.png").convert()
        self.villain = pygame.image.load("images/Gardien.png").convert()
        # fonction who creating the map
    def mapCreation(self):
        with open("structure_labyrinthe", "r") as structure:
            column = []
            l = 0
            for line in structure:
                lineStructure = []
                c =0

                for case in line:

                    if case != "\n":
                        for sprite in case:
                            spriteStructure = []
                            spriteStructure.append(c)
                            spriteStructure.append(l)
                            spriteStructure.append(case)
                        lineStructure.append(spriteStructure)
                        c += 1
                l += 1
                column.append(lineStructure)
            self.matrix = column
        #  place the objects randomly
        self.object = []
        while len(self.object) < 3:
            objectTemp = [random.randint(0, 14), random.randint(0, 14)]

            if self.matrix[objectTemp[1]][objectTemp[0]][2] == "0":
                self.object.append(objectTemp)
                self.matrix[objectTemp[1]][objectTemp[0]][2]= "obj"
        print(self.matrix)
        print(self.object)
        print(objectTemp)





        #fonction who display the map
    def displayMap(self):
        #displaying objects in the mapCreation
        self.window.blit(self.background, (0,0))
        self.window.blit(self.villain,(180, 420))
        self.window.blit(self.ether, ((self.object[0][0] * self.spriteSize) , (self.object[0][1] * self.spriteSize)))
        self.window.blit(self.needle, ((self.object[1][0] * self.spriteSize), (self.object[1][1] * self.spriteSize)))
        self.window.blit(self.tube, ((self.object[2][0] * self.spriteSize), (self.object[2][1] * self.spriteSize)))


        # displaying walls in the map
        l = 0
        for line in self.matrix:
            c = 0

            for case in line:

                if self.matrix[l][c][2] == "m":
                    self.window.blit(self.wall, ((c * self.spriteSize), (l * self.spriteSize)))
                c += 1
            l += 1
