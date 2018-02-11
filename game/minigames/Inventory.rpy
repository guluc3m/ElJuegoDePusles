init python:

#https://www.youtube.com/watch?v=kSO5iJGGFK0
#K_i sirve para capturar por pantalla

    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    class Inventory:
        def __init__(self):
            self.my_items = []
            self.max_size=15
            self.image=Image("images/Inventario/background.jpg")
            self.px_1=234
            self.py_1=186
        def has_item(self, item):
            if item in my_items:
                return True
            else:
                return False
        def add_item(self, Item):
            if len(my_items) < max_size:
                if has_item(Item.name) == False:
                    self.my_items.append(Item)
                    return True
                else:
                    print "Ya tienes este objeto en tu inventario"
                    return False
            else:
                print "No puedes guardar ese objeto porque ya tienes demasiados"
                return False
        def draw(self, screen, st, at, image):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.centerx), int(self.centery)))
            dist_x=195
            dist_y=195
            centr_x=77
            centr_y=78
            altura = 0
            posicion=0
            for item in my_items:
                #Pintamos cada objeto
                item.draw(pi, (centr_x+dist_x)*(posicion+1),
                (centr_y+dist_y)*altura)
                posicion+=1
                #Hacemos salto de línea si llega al final de la misma
                if posicion==5 or posicion==10:
                    altura+=1
                    posicion=0

    class Item(object):
        def __init__(self, name, image):
            self.arg = arg
            self.name=name
            self.image=Image(image)
            #self.description
        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.centerx), int(self.centery)))
        def use():
            pass

    class #Copia el PongDisplayable
