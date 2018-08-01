 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
""" Map games with Macgyver, search for three objects and exit.
Map generation and random placement of the three objects"""
import pygame
from pygame.locals import *
import class_map
from class_map import *
import sys



class Engine:

    def __init__(self):
        self.position_hero = []
        #self.hero = pygame.image.load("images/MacGyver.png").convert()

        #self.window = Map.window
        self.hero_up = pygame.image.load("images/personnage/up.png").convert_alpha()
        self.hero_down = pygame.image.load("images/personnage/down.png").convert_alpha()
        self.hero_right = pygame.image.load("images/personnage/right.png").convert_alpha()
        self.hero_left = pygame.image.load("images/personnage/left.png").convert_alpha()
        self.orientation = self.hero_down

    def position_of_hero(self, structure):
        for element in structure:
            for item in element:
                if item[2] == "d":
                    self.position_hero.append(item[0])
                    self.position_hero.append(item[1])

        #x = position_hero[0]
        #y = position_hero[1]

    def movement(self,structure, key):


        if key == 1:
            if (self.position_hero[1] + 1) < structure.nb_sprite:
                if structure.matrix[self.position_hero[1] + 1][self.position_hero[0]][2] != "m":
                    self.position_hero[1] += 1
                    self.orientation = self.hero_down
                    structure.window.blit(self.hero_down,
                                          (self.position_hero[0] * structure.sprite_size,
                                           self.position_hero[1] * structure.sprite_size))
        if key == 2:
            if (self.position_hero[1] - 1) < structure.nb_sprite:
                if structure.matrix[self.position_hero[1] - 1][self.position_hero[0]][2] != "m":
                    self.position_hero[1] -= 1
                    self.orientation = self.hero_up
                    structure.window.blit(self.hero_up,
                                          (self.position_hero[0] * structure.sprite_size,
                                           self.position_hero[1] * structure.sprite_size))
        if key == 3:
            if self.position_hero[0] + 1 < structure.nb_sprite:
                if structure.matrix[self.position_hero[1]][self.position_hero[0] + 1][2] != "m":
                    self.position_hero[0] += 1
                    self.orientation = self.hero_right
                    structure.window.blit(self.hero_right,
                                          (self.position_hero[0] * structure.sprite_size,
                                           self.position_hero[1] * structure.sprite_size))

        if key == 4:
            if self.position_hero[0] - 1 >= 0:
                if structure.matrix[self.position_hero[1]][self.position_hero[0] - 1][2] != "m":
                    self.position_hero[0] -= 1
                    self.orientation = self.hero_left
                    structure.window.blit(self.hero_left,
                                          (self.position_hero[0] * structure.sprite_size,
                                           self.position_hero[1] * structure.sprite_size))




    def end(self, structure, catalog, continuer):
        death = pygame.image.load("images/dead.png").convert_alpha()
        BRAVO = pygame.image.load("images/bravo.png").convert_alpha()
        POSITIONBRAVO = BRAVO.get_rect()
        POSITIONBRAVO.center = 225, 225
        GAMEOVER = pygame.image.load("images/game_over.png").convert_alpha()
        POSITIONGAMEOVER = GAMEOVER.get_rect()
        POSITIONGAMEOVER.center = 225, 225
        if structure.matrix[self.position_hero[1]][self.position_hero[0]][2] == "a" and catalog == 3:
            structure.window.blit(self.hero_down,
                                  (self.position_hero[0]*structure.sprite_size,
                                   self.position_hero[1]*structure.sprite_size))

            structure.window.blit(BRAVO, (POSITIONBRAVO))
            pygame.display.flip()
            pygame.time.wait(1000)
            continuer = 0
        if structure.matrix[self.position_hero[1]][self.position_hero[0]][2] == "a" and catalog != 3:
            structure.window.blit(structure.villain,
                                  (self.position_hero[0]*structure.sprite_size,
                                   self.position_hero[1]*structure.sprite_size))
            structure.window.blit(death,
                                  (self.position_hero[0]*structure.sprite_size,
                                   self.position_hero[1]*structure.sprite_size))
            pygame.time.wait(1000)
            structure.window.blit(GAMEOVER, (POSITIONGAMEOVER))
            pygame.display.flip()
            pygame.time.wait(1000)
            continuer = 0
            # structure.display_quit()
        return continuer


    def game(self):
        pygame.display.init()
        Laby = Map()
        Hero = Engine()

        Laby.display_home()
        level = Laby.display_level()
        Laby.map_structure(level)
        Laby.object_random()
        Laby.display_map()
        Hero.position_of_hero(Laby.matrix)
        Laby.window.blit(Hero.orientation,
                         (Hero.position_hero[0] * Laby.sprite_size,
                          Hero.position_hero[1] * Laby.sprite_size))
        pygame.display.flip()
        inventory = 0
        continuer = 1
        while continuer:

            Laby.display_map()
            pygame.time.Clock().tick(30)
            Laby.window.blit(Hero.orientation,
                             (Hero.position_hero[0] * Laby.sprite_size,
                              Hero.position_hero[1] * Laby.sprite_size))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer = 0
                    if event.key == K_DOWN:
                        Hero.movement(Laby, 1)
                    if event.key == K_UP:
                        Hero.movement(Laby, 2)
                        pygame.display.flip()
                    if event.key == K_RIGHT:
                        Hero.movement(Laby, 3)
                    if event.key == K_LEFT:
                        Hero.movement(Laby, 4)
                    if Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] == "ether":
                        Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] = "o"
                        Laby.window.blit(Laby.ether, (0, 600))
                        inventory += 1
                    if Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] == "needle":
                        Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] = "o"
                        Laby.window.blit(Laby.needle, (50, 600))
                        inventory += 1
                    if Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] == "tube":
                        Laby.matrix[Hero.position_hero[1]][Hero.position_hero[0]][2] = "o"
                        Laby.window.blit(Laby.tube, (100, 600))
                        inventory += 1
                    Laby.display_map()
                    Hero.end(Laby, inventory, continuer)
            continuer = Hero.end(Laby, inventory, continuer)
            if continuer == 0:
                Laby.display_quit(self)
            pygame.display.flip()
