 #!/usr/bin/env python
# -*- coding: utf-8 -*-
""" using the random module to randomly calculate positions"""
import random
"""utilisation de pygame pour l'affichage graphique du
   labyrinthe et les mouvement du héro"""
import pygame
from pygame.locals import *



class Map:

    """class that creates the map from the structure_labyrinth
    file and randomly calculates the positions of the three objects.
    it displays the map and all these elements except the hero"""

    def __init__(self):
        self.matrix = []
        self.window_size = 450
        self.nb_sprite = 15
        self.sprite_size = self.window_size / self.nb_sprite
        self.window = pygame.display.set_mode([450, 480])
        self.name_object = 0
        self.background = pygame.image.load("images/fond.jpg").convert()
        self.wall = pygame.image.load("images/mur2.png").convert()
        self.ether = pygame.image.load("images/ether.png").convert_alpha()
        self.needle = pygame.image.load("images/aiguille.png").convert()
        self.tube = pygame.image.load("images/tube.png").convert_alpha()
        self.villain = pygame.image.load("images/villain_ico.png").convert_alpha()
        self.home = pygame.image.load("images/home.jpg").convert_alpha()

    def map_structure(self):
        """create a table containing each position
           and the object assigned to it"""
        with open("structure_labyrinthe", "r") as structure:
            column = []
            line_column = 0
            for line in structure:
                line_structure = []
                case_column = 0
                for case in line:
                    if case != "\n":
                        for sprite in case:
                            sprite_structure = []
                            sprite_structure.append(case_column)
                            sprite_structure.append(line_column)
                            sprite_structure.append(case)
                        line_structure.append(sprite_structure)
                        case_column += 1
                line_column += 1
                column.append(line_structure)
            self.matrix = column

    def object_random(self):
        #  place the objects randomly
        self.object = []
        while len(self.object) < 3:
            object_temp = [random.randint(0, 14), random.randint(0, 14)]

            if self.matrix[object_temp[1]][object_temp[0]][2] == "0":
                self.object.append(object_temp)
                if self.name_object == 0:
                    self.matrix[object_temp[1]][object_temp[0]][2] = "ether"
                if self.name_object == 1:
                    self.matrix[object_temp[1]][object_temp[0]][2] = "needle"
                if self.name_object == 2:
                    self.matrix[object_temp[1]][object_temp[0]][2] = "tube"
                self.name_object += 1
    def display_object(self):
        y = 0
        for line in self.matrix:
            x = 0
            for case in line:
                if self.matrix[y][x][2] == "ether":
                    self.window.blit(self.ether, ((x * self.sprite_size),
                                                  (y * self.sprite_size)))
                if self.matrix[y][x][2] == "needle":
                    self.window.blit(self.needle, ((x * self.sprite_size),
                                                   (y * self.sprite_size)))
                if self.matrix[y][x][2] == "tube":
                    self.window.blit(self.tube, ((x * self.sprite_size),
                                                 (y * self.sprite_size)))
                x += 1
            y += 1

    def display_constant(self):

        line_constant = 0
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.villain, (180, 420))
        for line in self.matrix:
            case_constant = 0
            for case in line:
                if self.matrix[line_constant][case_constant][2] == "m":
                    self.window.blit(self.wall, ((case_constant*self.sprite_size),
                                                 (line_constant*self.sprite_size)))
                if self.matrix[line_constant][case_constant][2] == "a":
                    self.window.blit(self.villain, ((case_constant*self.sprite_size),
                                                    (line_constant*self.sprite_size)))
                case_constant += 1
            line_constant += 1

    def diplay_home(self):
        self.display_constant
        self.window.blit(selh.home, (0, 0))

    def display_map(self):
        """show all elements of the table,
           background, walls, object and wicked"""

        self.display_constant()
        self.display_object()
        # displaying walls in the map
