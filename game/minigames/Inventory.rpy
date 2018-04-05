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
            self.image=Image("images/Inventario/inventario_UIBG.png")
            #No recuerdo que es esto
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
                    print( "Ya tienes este objeto en tu inventario")
                    return False
            else:
                print( "No puedes guardar ese objeto porque ya tienes demasiados")
                return False

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            dist_x=195
            dist_y=195
            centr_x=0
            centr_y=0
            altura = 0
            posicion=0
            screen.blit(pi, (int(centr_x), int(centr_y)))
            for item in self.my_items:
                #Pintamos cada objeto
                item.centerx = (centr_x+dist_x)*(posicion+1)
                item.centery = (centr_y+dist_y)*altura
                item.draw(screen, st, at)
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
            self.centerx = 10
            self.centery = 10

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.centerx), int(self.centery)))

        def use():
            pass

    class InventoryDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            "Cargamos el inventario"
            self.inventory = Inventory()
            self.oldst = None


        def render(self, width, height, st, at):
            r=renpy.Render(width, height)

            self.oldst = st

            #if self.oldst is None:
            #    self.oldst = st

            renpy.redraw(self, 0)

            self.inventory.draw(r, st, at)

            return r


        def event(self, ev, x, y, st):
            keys=pygame.key.get_pressed()
            #dtime = st -self.oldst
            if keys[K_i]:
                return 0
            else:
                raise renpy.IgnoreEvent()

        def visit(self):
            return []
