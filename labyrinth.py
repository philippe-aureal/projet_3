from class_map import *
import pygame
from pygame.locals import *
# main file

#creation of object map
labyrinth = Map()
labyrinth.mapCreation()
# initialisation of pygame
#pygame.init()

pygame.init()
# affichage de la map

labyrinth.displayMap()
pygame.display.flip()
#boucle et mouvement du personnage
continuer = 1
while continuer:
    pygame.display.flip()





#rafraichissement de l'affichage
