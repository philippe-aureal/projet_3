 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
""" Labyrinth games with Macgyver, search for three objects and exit.
labyrinth generation and random placement of the three objects"""
import pygame
from pygame.locals import *

from class_map import Map
# main file

# creation of object map
LABYRINTH = Map()
LABYRINTH.map_creation()
LABYRINTH.object_random()
BRAVO = pygame.image.load("images/bravo.png").convert_alpha()
POSITIONBRAVO = BRAVO.get_rect()
POSITIONBRAVO.center = 225, 225
GAMEOVER = pygame.image.load("images/game_over.png").convert_alpha()
POSITIONGAMEOVER = GAMEOVER.get_rect()
POSITIONGAMEOVER.center = 225, 225
# affichage de la map

LABYRINTH.display_map()
HERO = pygame.image.load("images/MacGyver.png").convert()
position_hero = []
# position of hero

for element in LABYRINTH.matrix:
    for item in element:
        if item[2] == "d":
            position_hero.append(item[0])
            position_hero.append(item[1])
x = position_hero[0]
y = position_hero[1]

LABYRINTH.window.blit(HERO,
                      (x * LABYRINTH.sprite_size, y * LABYRINTH.sprite_size))

pygame.display.flip()
# boucle et mouvement du personnage
inventory = 0
continuer = 1
while continuer:

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0
    # lead the hero
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if (y + 1) < LABYRINTH.nb_sprite:
                    if LABYRINTH.matrix[y + 1][x][2] != "m":
                        y += 1
            if event.key == K_UP:
                if (y - 1) >= 0:
                    if LABYRINTH.matrix[y - 1][x][2] != "m":
                        y -= 1
            if event.key == K_RIGHT:
                if x + 1 < LABYRINTH.nb_sprite:
                    if LABYRINTH.matrix[y][x + 1][2] != "m":
                        x += 1
            if event.key == K_LEFT:
                if x - 1 >= 0:
                    if LABYRINTH.matrix[y][x - 1][2] != "m":
                        x -= 1
        # recuperation of objects
            if LABYRINTH.matrix[y][x][2] == "ether":
                LABYRINTH.matrix[y][x][2] = "o"
                inventory += 1
            if LABYRINTH.matrix[y][x][2] == "needle":
                LABYRINTH.matrix[y][x][2] = "o"
                inventory += 1
            if LABYRINTH.matrix[y][x][2] == "tube":
                LABYRINTH.matrix[y][x][2] = "o"
                inventory += 1
            if LABYRINTH.matrix[y][x][2] == "a" and inventory == 3:
                LABYRINTH.window.blit(BRAVO, (POSITIONBRAVO))
                pygame.display.flip()
                pygame.time.wait(5000)
                continuer = 0

    LABYRINTH.display_map()
    LABYRINTH.window.blit(HERO,
                          (x * LABYRINTH.sprite_size, y * LABYRINTH.sprite_size))
    if LABYRINTH.matrix[y][x][2] == "a" and inventory != 3:
        LABYRINTH.matrix[y][x][2] = "a"
        LABYRINTH.window.blit(LABYRINTH.villain,
                              (x*LABYRINTH.sprite_size, y*LABYRINTH.sprite_size))
        LABYRINTH.window.blit(GAMEOVER, (POSITIONGAMEOVER))
        pygame.display.flip()
        pygame.time.wait(5000)
        continuer = 0

# rafraichissement de l'affichage
    pygame.display.flip()
