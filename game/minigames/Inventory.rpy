init python:

    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    SIZE = 160

    class Inventory:
        def __init__(self):
            self.my_items = []
            self.my_names=[]
            for i in self.my_items:
                self.my_names.append(i.name)
            self.max_size=15
            #Actualizar la imagen
            self.image=im.Scale("images/Inventario/inventario_UIBG.png", WIDTH, HEIGHT)

            self.initx=160
            self.inity=85

        def has_item(self, name):
            if name in self.my_names:
                return True
            else:
                return False

        def add_item(self, Item):
            if len(self.my_items) < self.max_size:
                if not self.has_item(Item.name):
                    self.my_items.append(Item)
                    return True
                else:
                    print("Ya tienes este objeto en tu inventario")
                    return False
            else:
                print("No puedes guardar ese objeto porque ya tienes demasiados")
                return False

        def remove_item(self, Item):
            self.my_items.remove(Item)
            self.my_names.remove(Item.name)

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (0, 0))
            dist_x=40
            dist_y=35

            altura = 0
            posicion=0

            for item in self.my_items:
                #Asignamos las coordenadas de cada celda
                item.topleft_x = self.initx+(dist_x*posicion)+(SIZE*posicion)
                item.topleft_y = self.inity+(dist_y*altura)+(SIZE*altura)
                posicion+=1
                #Hacemos salto de línea si llega al final de la misma
                if posicion>=5:
                    altura+=1
                    posicion=0
                item.draw(screen, st, at)

    class Item(object):
        def __init__(self, name, image, description):
            self.name=str(name)
            self.image=im.Scale(image, SIZE, SIZE)
            self.description=str(description)
            self.topleft_x = 0
            self.topleft_y = 0
            self.paint_description = False

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.topleft_x), int(self.topleft_y)))

    class InventoryDisplayable(renpy.Displayable):
        def __init__(self, inventory):
            renpy.Displayable.__init__(self)

            #Cargamos el inventario
            self.inventory = inventory
            self.oldst = None

        def render(self, width, height, st, at):
            r=renpy.Render(width, height)

            # Para poder saber el tiempo
            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st

            renpy.redraw(self, 0)

            self.inventory.draw(r, st, at)

            for i in self.inventory.my_items:
                if i.paint_description:
                    description = renpy.render(Text(i.description, size=36), WIDTH, HEIGHT, st, at)
                    r.blit(description, (WIDTH/2-200, 25))

            return r

        def event(self, ev, x, y, st):
            keys=pygame.key.get_pressed()
            #dtime = st -self.oldst
            if keys[K_i]:
                return 0

            #mouse.get_pos() deuelve un valor para cada coordenada, de ahí ambas variables
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print('Mouse(x,y):' + str(mouse_x) + ' ' +  str(mouse_y))

            #if pygame.mouse.get_pressed()[0]:
            for i in self.inventory.my_items:
                if (mouse_x in range(i.topleft_x+57, i.topleft_x+216+57)) and (mouse_y in range(i.topleft_y+31, i.topleft_y+216+31)):

                    i.paint_description=True
                else :
                    i.paint_description=False

        def visit(self):
            return []
