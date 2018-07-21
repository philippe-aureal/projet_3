from class_map import *
import pygame
from pygame.locals import *
# main file

#creation of object map
labyrinth = Map()
labyrinth.mapCreation()
# initialisation of pygame
print(labyrinth.matrix)


pygame.init()
# affichage de la map

labyrinth.displayMap()
hero = pygame.image.load("images/MacGyver.png").convert()
positionHero = []

print(labyrinth.matrix)
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
















    labyrinth.displayMap()
    labyrinth.window.blit(hero, (x * labyrinth.spriteSize, y * labyrinth.spriteSize))








    pygame.display.flip()





#rafraichissement de l'affichage
