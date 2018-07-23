from class_map import *
import pygame
from pygame.locals import *
# main file

#creation of object map
labyrinth = Map()
labyrinth.mapCreation()
# initialisation of pygame

inventaire = 0


pygame.init()
# affichage de la map

labyrinth.displayMap()
hero = pygame.image.load("images/MacGyver.png").convert()
positionHero = []
# position of hero

for element in labyrinth.matrix:
    for item in element:
        if item[2] == "d":
            positionHero.append(item[0])
            positionHero.append(item[1])
x = positionHero[0]
y = positionHero[1]

labyrinth.window.blit(hero, (x * labyrinth.spriteSize, y * labyrinth.spriteSize))

pygame.display.flip()
#boucle et mouvement du personnage
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0
    #lead the hero
        if event.type == KEYDOWN:
            if event.key == K_DOWN:

                if (y + 1) < labyrinth.nbSprite:
                    if labyrinth.matrix[y + 1][x][2] != "m":
                        y += 1

            if event.key == K_UP:
                if (y - 1) >= 0:
                    if labyrinth.matrix[y - 1][x][2] != "m":
                        y -= 1
            if event.key == K_RIGHT:
                if x + 1 < labyrinth.nbSprite:
                    if labyrinth.matrix[y][x + 1][2] != "m":
                        x += 1
            if event.key == K_LEFT:
                if x - 1 >= 0:
                    if labyrinth.matrix[y][x - 1][2] != "m":
                        x -= 1
        #recuperation of objects
            if labyrinth.matrix[y][x][2] == "ether":
                labyrinth.matrix[y][x][2] = "o"
                inventaire += 1
            if labyrinth.matrix[y][x][2] == "needle":
                labyrinth.matrix[y][x][2] = "o"
                inventaire += 1
            if labyrinth.matrix[y][x][2] == "tube":
                labyrinth.matrix[y][x][2] = "o"
                inventaire += 1

            if labyrinth.matrix[y][x][2] == "a" and inventaire == 3:
                continuer = 0



    labyrinth.displayMap()
    labyrinth.window.blit(hero, (x * labyrinth.spriteSize, y * labyrinth.spriteSize))


#rafraichissement de l'affichage
    pygame.display.flip()
