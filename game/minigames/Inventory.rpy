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
            screen.blit(pi, (0, 0))
            dist_x=185
            dist_y=195
            if len(self.my_items)>0:
                topleft_x=self.my_items[0].topleft_x
                topleft_y=self.my_items[0].topleft_y

            altura = 0
            posicion=0

            for item in self.my_items:
                #Pintamos cada objeto
                item.topleft_x = topleft_x+(dist_x*posicion)
                item.topleft_y = topleft_y+(dist_y*altura)
                posicion+=1
                #Hacemos salto de línea si llega al final de la misma
                if posicion>=5:
                    altura+=1
                    posicion=0
                item.draw(screen, st, at)

    class Item(object):
        def __init__(self, name, image, description):
            #self.arg = arg
            self.name=str(name)
            self.image=im.Scale(image, 160, 160)
            self.description=description
            self.topleft_y = 86
            self.topleft_x = 175
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

            #if pygame.mouse.get_pressed()[0]:
            for i in self.inventory.my_items:
                if mouse_x in range(i.topleft_x, i.topleft_x+160) and mouse_y in range(i.topleft_y, i.topleft_y + 160):
                    print(mouse_x, mouse_y, i.topleft_x, i.topleft_y)
                    i.paint_description=True
                else :
                    i.paint_description=False

        def visit(self):
            return []
