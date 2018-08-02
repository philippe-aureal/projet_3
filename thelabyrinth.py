#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Map games with Macgyver, search for three objects and exit.
 Map generation and random placement of the three objects"""
import pygame
from pygame.locals import *

from class_map import Map
import class_engine
from class_engine import *
import sys


if __name__ == "__main__":


    Hero = Engine()
    Hero.game()
    #Engine.game(Engine)
