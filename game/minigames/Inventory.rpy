init python:

    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    class Inventory:
        def __init__(self):
            self.my_items = []
            self.max_size=15
            #Actualizar la imagen
            self.image=Image("images/Inventario/inventario_UIBG.png")

        def has_item(self, item):
            if item in self.my_items:
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

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            dist_x=195
            dist_y=195
            if len(self.my_items)>0:
                center_x=self.my_items[0].centerx
                center_y=self.my_items[0].centery
            else:
                center_x=0
                center_y=0
            altura = 0
            posicion=0
            screen.blit(pi, (int(center_x), int(center_y)))
            
            for item in self.my_items:
                #Pintamos cada objeto
                item.centerx = (center_x+dist_x)*(posicion+1)
                item.centery = (center_y+dist_y)*(altura+1)
                posicion+=1
                #Hacemos salto de línea si llega al final de la misma
                if posicion>=5:
                    altura+=1
                    posicion=0

    class Item(object):
        def __init__(self, name, image, description):
            #self.arg = arg
            self.name=str(name)
            self.image=Image(image)
            self.description=description
            self.centerx = 120
            self.centery = 120

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            screen.blit(pi, (int(self.centerx), int(self.centery)))

    class InventoryDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            #Cargamos el inventario
            self.inventory = Inventory()
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
                self.inventory.my_items[i].draw(r, st, at)

            return r


        def event(self, ev, x, y, st):
            keys=pygame.key.get_pressed()
            #dtime = st -self.oldst
            if keys[K_i]:
                return 0
            else:
                raise renpy.IgnoreEvent()

            #mouse.get_pos() deuelve un valor para cada coordenada, de ahí ambas variables
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed():
                for i in range(0,15):
                    if mouse_x == range(self.my_items[i].centerx-120, self.my_items[i].centerx+120) and mouse_y == range(self.my_items[i].centery-120, self.my_items[i].centery+120) and pygame.mouse.get_pressed():
                        description = renpy.render(Text(self.my_items[i].description, size=36), WIDTH, HEIGHT, st, at)
                        r.blit(description, (WIDTH/2-100, 25))
        def visit(self):
            return []
