    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    class snake_part():
        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            if self.height is None:
                piw, self.height = pi.get_size()
            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.x), int(self.y)))

        def __init__(self, x, y, image):
            self.image=image
            self.x=x
            self.y=y



    class node():
        def __init__(self):
            self.elem=None
            #El snake part encapsulado
            self.next=None
                #a priori self.next es None y ya se ira llenando conforme coma

    class snake_complete():
        def __init__(self):
            self.first=None
            #self.first es la cabesa
            self.last=None
            self.length=1


    class food():
        def __init__(self, x, y, image):
            self.x=x
            self.y=y
            self.image=image


    class juego():
        pass
