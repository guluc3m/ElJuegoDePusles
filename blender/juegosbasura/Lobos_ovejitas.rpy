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
            self.width = HEIGHT/6
            self.bicho1
            self.bicho2


        def mover(self, time, keys):
            if keys[K_RIGHT] && self.centerx = WEIGHT/4: #Orilla izquierda a derecha
                self.centerx = WEIGHT/4*3

            if keys[K_LEFT] && self.centerx = WEIGHT/4: #Orilla derecha a izquierda
                self.centerx = WEIGHT/4

            #if self.centery >= 0:
            #    # Flechita hacia la derecha
            #    if keys[K_RIGHT] && self.centerx = WEIGHT/4: #Orilla derecha
            #        self.centerx = WEIGHT/4*3
            #
            #    if keys[K_LEFT] && self.centerx >= WEIGHT/4*3:  #Orilla izquierda
            #        self.centerx = WEIGHT/4

            def draw(self, screen, st, at):
                pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                screen.blit(pi, (int(self.centerx), int(self.centery)))

    class Lobos():
        def _init_(self, px):
            self.image = Image(".png")
            self.centerx = WIDTH/5
            self.centery = HEIGHT/2  #Lo sitúo a la izquierda por debajo de la mitad de la pantalla
            self.height = HEIGHT/6
            self.width = WIDTH/10  #Por ejemplo
            self.selected = False;


        def mover(self, time, keys):
            if self.selected == True:
                self.centerx = Balsa.self.centerx;
                if keys[K_RIGHT] && self.centerx == WEIGHT/5: #Orilla izquierda a derecha
                    self.centerx = WEIGHT/5*4

                if keys[K_LEFT] && self.centerx == WEIGHT/5*4: #Orilla derecha a izquierda
                    self.centerx = WEIGHT/5

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))

    class Ovejas():
        def _init_(self, px):
            self.image = Image(".png")
            self.centerx = WIDTH/5
            self.centery = HEIGHT/2 -5 #Lo sitúo debajo de los lobos
            self.height = HEIGHT/6
            self.width = WIDTH/10  #Por ejemplo
            self.selected = False;

        def mover(self, time, keys):
            if(self.selected == True)
                if keys[K_RIGHT] && self.centerx = WIDTH/5: #Orilla izquierda a derecha
                    self.centerx = WIDTH/5*4

                if keys[K_LEFT] && self.centerx = WIDTH/5*4: #Orilla derecha a izquierda
                    self.centerx = WIDTH/5

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))


    class Lobos_ovejitas_Displayable(renpy.Displayable):

        def __init__(self):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            renpy.Displayable.__init__(self)

            #Elementos a mostrar
            ''' Carga de la balsa '''
            self.Balsa = balsa()

            ''' Carga de los 3 lobos '''
            lobitos = []
            for i in range(0,3):
                lobitos.append(Lobos())

            ''' Carga de las 3 ovejas '''
            lobitos = []
            for i in range(0,3):
                lobitos.append(Ovejas())


            def render(self, width, height, st, at):
                # Similar al screen de pygame
                r = renpy.Render(width, height)

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.start, WIDTH, HEIGHT, st, at)
                    ctbw, ctbh = ctb.get_size()
                    r.blit(ctb, (WIDTH/2-ctbw/2, HEIGHT/2))

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                for i in range(0,3):
                self.lobitos[i].draw(r, st, at)

                for i in range(0,3):
                self.ovejas[i].draw(r, st, at)

                self.balsa.draw(r, st, at)

                # Return the Render object.
                return r
