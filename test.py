from class_map import *
import pygame
from pygame.locals import *



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
    matrix = column
    print(matrix.index("d"))
