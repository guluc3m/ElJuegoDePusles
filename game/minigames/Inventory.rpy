init python:

#https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=15475

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
            self.rows=3
            self.columns=5
            self.px_1=234
            self.py_1=186
        def has_item(self, item):
            if item in my_items:
                return True
            else:
                return False
        def add_item(self, item):
            if len(my_items) < max_size:
                if has_item(item.name) == False:
                    self.my_items.append(item)
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
            my_items=
            dist_x=195
            dist_y=195
            #Vamos a decir que el centro del objeto es x y para colocarlo vamos a poner my_items[posición].draw((x+distanciax)*posición)
            #para ponerlo al lado del objeto anterior y si llega al final variar la altura y volver al ancho del principio
            #Así se van a ir reordenando todo el rato

    class Item(object):
        def __init__(self, name, image, px, py):
            self.arg = arg
            self.name=name
            self.image=image
            self.centerx = px
            self.centery = py
            #self.description
        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.centerx), int(self.centery)))
        def use():
            pass

    class Cell(object):
        def __init__(self):
            self.px=71
            self.py=78
            self.placed=false
