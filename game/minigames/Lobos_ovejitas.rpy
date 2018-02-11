init python:

    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    #Esto dibuja la balsa

    class Balsa():
        def __init__(self, px):
            self.image = Image(".png")
            self.centerx = WIDTH/4
            self.centery = HEIGHT/2  #Lo sitúo a la izquierda por debajo de la mitad de la pantalla
            self.height = HEIGHT/6


        def mover(self, time, keys):



            #if self.centery >= 0:
            #    # Flechita hacia la derecha
            #    if keys[K_RIGHT] && self.centerx = WEIGHT/4: #Orilla derecha
            #        self.centerx = WEIGHT/4*3
            #
            #    if keys[K_LEFT] && self.centerx >= WEIGHT/4*3:  #Orilla izquierda
            #        self.centerx = WEIGHT/4
