init python:

    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    #Esto dibuja la balsa
'''como hago el recuento de lobos y ovejas en cada orilla???'''

    class Balsa():
        def __init__(self):
            self.image = Image(".png")
            self.centerx = WIDTH/4
            self.centery = HEIGHT/2  #Lo sitúo a la izquierda por debajo de la mitad de la pantalla
            self.height = HEIGHT/6
            self.width = HEIGHT/6
            self.bicho1 = None
            self.bicho2 = None
            self.orilla_izq = True
            self.permiso_mover = True '''creo que lo voy a usar para la duda de arriba'''

            '''necesito funcion para las posiciones de los bichos'''
        '''necesito def subir_animalicos_a_la_barca'''

        def seleccionado(self, animalico):
            if(animalico.selected == False):
                self.lobitos[i].self.selected = True
                if(self.bicho1 == None):
                    self.bicho1 = self.lobitos[i]
                else:
                    self.bicho2 = self.lobitos[i]
            else:
                self.lobitos[i].self.selected = False


        def subir_animalicos_a_la_barca(self, animalico):
        #    self.lobitos[i].self.centerx = self.balsa.self.centerx    #Igualar la pos raton a animalicos para ponerlos sobre la balsa


        def mover(self, time, keys):
            if (keys[K_RIGHT] && self.centerx = WEIGHT/4): #Orilla izquierda a derecha
                self.centerx = WEIGHT/4*3

            if (keys[K_LEFT] && self.centerx = WEIGHT/4): #Orilla derecha a izquierda
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


    class Animalicos():

        def _init_(self):
          self.image = Image(".png")
          self.centerx = (WIDTH/5)
          self.centery = HEIGHT/2  #Lo sitúo a la izquierda por debajo de la mitad de la pantalla
          self.height = HEIGHT/6
          self.width = WIDTH/10  #Por ejemplo
          self.selected = False
          self.orilla_izq = True

        def mover(self, time, keys):
            if (self.selected == True):
                 self.centerx = Balsa.self.centerx;
                 if (keys[K_RIGHT] && self.centerx == WEIGHT/5): #Orilla izquierda a derecha
                     self.centerx = WEIGHT/5*4
                     self.selected = False

                 if (keys[K_LEFT] && self.centerx == WEIGHT/5*4): #Orilla derecha a izquierda
                     self.centerx = WEIGHT/5
                     self.selected = False

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))


    class Lobos(Animalicos):

        def _init_(self, desplazamiento):
            super(Lobos, self).__init__(self)



    class Ovejas(Animalicos):

        def _init_(self, desplazamiento):
            super(Ovejas, self).__init__(self)



    class Lobos_ovejitas_Displayable(renpy.Displayable):

        def __init__(self):

            pygame.mouse.set_visible()
            # Pass additional properties on to the renpy.Displayable
            # constructor.

            renpy.Displayable.__init__(self)

            ''' Carga de la balsa '''
            self.balsa = Class_Balsa()

            ''' Carga de los 3 lobos y las 3 ovejas '''
            self.animales = []
            for i in range(0,3):
                animales.append(Lobos(10*i))


            ''' Carga de las 3 ovejas '''
            self.ovejitas = []
            for i in range(0,3): '''Separo cada lobo 10 pixeles  ¿esta bien? --> SIIII'''
                self.ovejitas.append(Oveja(10*i))
                #self.ovejitas[i].self.centerx += 10*i





            '''Pinto todo'''
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





        def events(): #Clicar sobre animalicos
            if pygame.mouse.get_pressed():
                for i in range(0,3):
                    if pygame.mouse.get_pos()[0] == self.lobitos[i].self.centerx &&  pygame.mouse.get_pos()[1] == self.lobitos[i].self.centery:# && self.lobitos[i].self.orilla_izq == self.balsa.self.orilla_izq:
                        self.barca.subir_animalicos_a_la_barca(lobitos[i])



#debo crear funcion en el displayable para el movimiento?????? --> SI


        def movement(self, time, keys):
            for i in range(0.3):
                self.lobitos[i].mover(self, time, keys)

            for i in range(0,3):
                self.ovejitas[i].mover(self, time, keys)
