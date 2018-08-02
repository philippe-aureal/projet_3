 #!/usr/bin/env python
# -*- coding: utf-8 -*-
""" using the random module to randomly calculate positions"""
import random
"""utilisation de pygame pour l'affichage graphique du
   labyrinthe et les mouvement du héro"""
import pygame
from pygame.locals import *
import sys



class Map:

    """class that creates the map from the structure_labyrinth
    file and randomly calculates the positions of the three objects.
    it displays the map and all these elements except the hero"""

    def __init__(self):
        self.matrix = []
        self.window_size = 600
        self.nb_sprite = 15
        self.sprite_size = self.window_size / self.nb_sprite
        self.window = pygame.display.set_mode((600, 640))
        self.name_object = 0
        self.background = pygame.image.load("images/fond.jpg").convert()
        self.background2 = pygame.image.load("images/fond2.jpg").convert()
        self.wall = pygame.image.load("images/mur2.png").convert()
        self.ether = pygame.image.load("images/ether.png").convert_alpha()
        self.needle = pygame.image.load("images/aiguille.png").convert_alpha()
        self.tube = pygame.image.load("images/tube.png").convert_alpha()
        self.villain = pygame.image.load("images/villain_ico.png").convert_alpha()
        self.home = pygame.image.load("images/home.jpg").convert_alpha()
        self.menu = pygame.image.load("images/menu.png").convert_alpha()
        self.after_game = pygame.image.load("images/after_game.png").convert_alpha()
        self.menu2 = pygame.image.load("images/menu2.png").convert_alpha()


    def map_structure(self, level):
        """create a table containing each position
           and the object assigned to it"""
        if level == 1:
            level_structure = "structure_labyrhinte"
        else:
            level_structure = "structure_labyrhinte2"
        with open(level_structure, "r") as structure:
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
        #self.window.blit(self.villain, (180, 420))
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

    def display_home(self):
        self.window.blit(self.home, (0, 0))
        self.window.blit(self.menu, (142, 420))
        pygame.display.flip()
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        continuer = 0
                    if event.key == K_ESCAPE:
                        sys.exit(0)

    def display_level(self):
        self.window.blit(self.home, (0, 0))
        self.window.blit(self.menu2, (142, 370))
        pygame.display.flip()
        continu = 1
        while continu:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_F1:
                    continu = 0
                    level = 1


                if event.type == KEYDOWN and event.key == K_F2:
                    level = 2
                    continu = 0
        return level


    def display_quit(self, fonct):
        self.display_map()
        self.window.blit(self.background2, (0, 0))
        self.window.blit(self.after_game, (0, 0))
        pygame.display.flip()
        loop = 1
        while loop:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        fonct.game()
                        loop = 0
                    if event.key == K_ESCAPE:
                        # sys.exit(0)
                        loop = 0
            pygame.display.flip()




    def display_map(self):
        """show all elements of the table,
           background, walls, object and wicked"""

        self.display_constant()
        self.display_object()
        # displaying walls in the map
