#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" The pygame module is used for displaying the graphical interface and
    manage the keyboard events
    The class_map module provides the structure containing
    the positions of each objects

"""
import pygame
from pygame.locals import *
from class_map import Map


class Engine:
    """class that manages the position of the hero, his movements and the
       events consequent to his position
    """

    def __init__(self):
        self.position_hero = []

    def position_of_hero(self, structure):
        """ method who search the initial position of
            hero in structure file
        """
        for element in structure:
            for item in element:
                if item[2] == "d":
                    self.position_hero.append(item[0])
                    self.position_hero.append(item[1])

    def movement(self, structure, key):
        """ method that calculates and display the position of
            the hero after a keyboard event
        """
        if key == 1:
            if (self.position_hero[1] + 1) < structure.nb_sprite:
                if structure.matrix[self.position_hero[1] + 1
                                    ][self.position_hero[0]][2] != "m":
                    self.position_hero[1] += 1
                    self.orientation = self.hero_down
                    structure.window.blit(self.hero_down,
                                          (self.position_hero[0] *
                                           structure.sprite_size,
                                           self.position_hero[1] *
                                           structure.sprite_size))
        if key == 2:
            if (self.position_hero[1] - 1) >= 0:
                if structure.matrix[self.position_hero[1] - 1
                                    ][self.position_hero[0]][2] != "m":
                    self.position_hero[1] -= 1
                    self.orientation = self.hero_up
                    structure.window.blit(self.hero_up,
                                          (self.position_hero[0] *
                                           structure.sprite_size,
                                           self.position_hero[1] *
                                           structure.sprite_size))
        if key == 3:
            if self.position_hero[0] + 1 < structure.nb_sprite:
                if structure.matrix[self.position_hero[1]
                                    ][self.position_hero[0] + 1][2] != "m":
                    self.position_hero[0] += 1
                    self.orientation = self.hero_right
                    structure.window.blit(self.hero_right,
                                          (self.position_hero[0] *
                                           structure.sprite_size,
                                           self.position_hero[1] *
                                           structure.sprite_size))

        if key == 4:
            if self.position_hero[0] - 1 >= 0:
                if structure.matrix[self.position_hero[1]
                                    ][self.position_hero[0] - 1][2] != "m":
                    self.position_hero[0] -= 1
                    self.orientation = self.hero_left
                    structure.window.blit(self.hero_left,
                                          (self.position_hero[0] *
                                           structure.sprite_size,
                                           self.position_hero[1] *
                                           structure.sprite_size))

    def end(self, structure, catalog, continuer):
        """ method who display the differents final event of the game"""

        death = pygame.image.load("images/dead.png").convert_alpha()
        bravo = pygame.image.load("images/bravo.png").convert_alpha()
        position_bravo = bravo.get_rect()
        position_bravo.center = 225, 225
        gameOver = pygame.image.load("images/game_over.png").convert_alpha()
        position_gameover = gameOver.get_rect()
        position_gameover.center = 225, 225
        # end and victory
        if structure.matrix[
                self.position_hero[1]][self.position_hero[0]
                                       ][2] == "a" and catalog == 3:
            structure.window.blit(self.hero_down,
                                  (self.position_hero[0] *
                                   structure.sprite_size,
                                   self.position_hero[1] *
                                   structure.sprite_size))
            structure.window.blit(bravo, (position_bravo))
            pygame.display.flip()
            pygame.time.wait(1000)
            continuer = 0
        # end and lost
        if structure.matrix[
                self.position_hero[1]][self.position_hero[0]
                                       ][2] == "a" and catalog != 3:
            structure.window.blit(structure.villain,
                                  (self.position_hero[0]*structure.sprite_size,
                                   self.position_hero[1] *
                                   structure.sprite_size))
            structure.window.blit(death,
                                  (self.position_hero[0]*structure.sprite_size,
                                   self.position_hero[1] *
                                   structure.sprite_size))
            pygame.time.wait(1000)
            structure.window.blit(gameOver, (position_gameover))
            pygame.display.flip()
            pygame.time.wait(1000)
            continuer = 0
        return continuer

    def game(self):
        """method that manages the game engine by keyboard events"""
        pygame.display.init()
        Laby = Map()
        # loading hero's orientation images
        self.hero_up = pygame.image.load(
            "images/personnage/up.png").convert_alpha()
        self.hero_down = pygame.image.load(
            "images/personnage/down.png").convert_alpha()
        self.hero_right = pygame.image.load(
            "images/personnage/right.png").convert_alpha()
        self.hero_left = pygame.image.load(
            "images/personnage/left.png").convert_alpha()
        self.orientation = self.hero_down

        Laby.display_home()

        loop2 = 1
        # loop that display all elements of the map
        while loop2:
            Laby = Map()
            level = Laby.display_level()
            Laby.map_structure(level)
            self.position_hero = []
            self.position_of_hero(Laby.matrix)
            Laby.object_random()
            Laby.display_map()
            Laby.window.blit(self.orientation,
                             (self.position_hero[0] * Laby.sprite_size,
                              self.position_hero[1] * Laby.sprite_size))
            pygame.display.flip()
            inventory = 0
            continuer = 1
            # Keyboard events loop for moving the hero
            while continuer:

                Laby.display_map()
                pygame.time.Clock().tick(30)
                Laby.window.blit(self.orientation,
                                 (self.position_hero[0] * Laby.sprite_size,
                                  self.position_hero[1] * Laby.sprite_size))
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            continuer = 0
                        if event.key == K_DOWN:
                            self.movement(Laby, 1)
                        if event.key == K_UP:
                            self.movement(Laby, 2)
                        if event.key == K_RIGHT:
                            self.movement(Laby, 3)
                        if event.key == K_LEFT:
                            self.movement(Laby, 4)
                        # deleting the map object if it is picked up
                        # and display in the bottom menu
                        if Laby.matrix[
                                self.position_hero[1]][self.position_hero[0]
                                                       ][2] == "ether":
                            Laby.matrix[self.position_hero[1]
                                        ][self.position_hero[0]][2] = "o"
                            Laby.window.blit(Laby.ether, (0, 600))
                            inventory += 1
                        if Laby.matrix[
                                self.position_hero[1]][self.position_hero[0]
                                                       ][2] == "needle":
                            Laby.matrix[self.position_hero[1]
                                        ][self.position_hero[0]][2] = "o"
                            Laby.window.blit(Laby.needle, (50, 600))
                            inventory += 1
                        if Laby.matrix[
                                self.position_hero[1]][self.position_hero[0]
                                                       ][2] == "tube":
                            Laby.matrix[self.position_hero[1]
                                        ][self.position_hero[0]][2] = "o"
                            Laby.window.blit(Laby.tube, (100, 600))
                            inventory += 1
                        Laby.display_map()
                        self.end(Laby, inventory, continuer)
                continuer = self.end(Laby, inventory, continuer)
                if continuer == 0:
                    Laby.display_quit(self)
                pygame.display.flip()
