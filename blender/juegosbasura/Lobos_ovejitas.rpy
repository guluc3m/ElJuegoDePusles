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
            self.time = -1
            self.image = Image("balsa.png")
            self.centerx = WIDTH/4
            self.centery = HEIGHT/2  #Lo sitúo a la izquierda por debajo de la mitad de la pantalla
            self.height = HEIGHT/6
            self.width = HEIGHT/6
            self.flag = False
            self.bicho1 = None
            self.bicho2 = None
            self.orilla_izq = True
            self.permiso_mover = True




        def seleccionado(self, animalico):
            if(animalico.selected == False):
                animalico.selected = True
                if(self.bicho1 == None):
                    self.bicho1 = animalico
                elif(self.bicho != None && self.bicho2 == None):
                    self.bicho2 = animalico
                else:

                    self.flag==True

            else:
                self.animales[i].selected = False


        def subir_animalicos_a_la_barca(self):
            if (self.bicho1 != None):
                self.bicho1.centerx = self.centerx
                self.bicho1.centery = self.centery
            if(self.bicho2 != None):
                self.bicho2.centerx = self.centerx +10
                self.bicho2.centerx = self.centery




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
            if(self.flag == True):
                not_possible = renpy.render(Text("Not possible", size=36), WIDTH, HEIGHT, st, at)
                r.blit(not_possible, (WIDTH/2-100, 25))
                if(self.time == -1):
                    self.time = st
                elif(st - self.time > 1.5):
                    self.flag = False
                    self.time = -1


    class Animalico():

        def __init__(self):
          self.image = Image("lobo.png")
          self.centerx = (WIDTH/5)
          self.centery = HEIGHT/2  '''Lo sitúo a la izquierda por debajo de la mitad de la pantalla'''
          self.height = HEIGHT/6
          self.width = WIDTH/10  #Por ejemplo
          self.selected = False
          self.orilla_izq = True

        def mover(self, time, keys):
            if (self.selected == True):
                 self.centerx = Balsa.centerx;
                 if (keys[K_RIGHT] && self.centerx == WEIGHT/5): '''Orilla izquierda a derecha'''
                     self.centerx = WEIGHT/5*4
                     self.selected = False

                 if (keys[K_LEFT] && self.centerx == WEIGHT/5*4): '''Orilla derecha a izquierda'''
                     self.centerx = WEIGHT/5
                     self.selected = False

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))


    class Lobo(Animalico):

        def __init__(self, desplazamiento):
            super(Lobo, self).__init__(self)
            self.image = Image("lobo.png")
            self.centerx = self.centerx + desplazamiento


    class Oveja(Animalico):

        def __init__(self, desplazamiento):
            super(Oveja, self).__init__(self)
            self.image = Image("oveja.png")
            self.centery = self.centery - 10
            self.centerx = self.centerx + desplazamiento



    class Lobos_ovejitas_Displayable(renpy.Displayable):

        def __init__(self):

            pygame.mouse.set_visible()
            # Pass additional properties on to the renpy.Displayable
            # constructor.

            renpy.Displayable.__init__(self)

            ''' Carga de la balsa '''
            self.balsa = Balsa()

            ''' Carga de los 3 lobos y las 3 ovejas '''
            self.animales = []
            for i in range(0,6):
                animales.append(Lobo(10*i))
                animales.append(Oveja(10*i))

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

            for i in range(0,6):
            self.animales[i].draw(r, st, at)
            self.balsa.draw(r, st, at)
            # Return the Render object.
            return r




        '''Clicar sobre animalicos'''
        def event(self, ev, x, y, st):
            if pygame.mouse.get_pressed():
                for i in range(0,6):
                    if(pygame.mouse.get_pos()[0] == self.animales[i].centerx &&
                    pygame.mouse.get_pos()[1] == self.animales[i].centery &&
                    self.animales[i].orilla_izq == self.balsa.orilla_izq):
                        self.barca.seleccionado(self,self.animales[i])
                        self.barca.subir_animalico_a_la_barca(self)



        #debo crear funcion en el displayable para el movimiento?????? --> SI

        def check_rules(self):
            num_lobos = 0
            nom_ovejas = 0
            for i in range(0,6):
                if(isinstance(self.animales[i], Lobo)):
                    num_lobos += 1
                elif(isinstance(self.animales[i], Oveja)):
                    num_ovejas += 1




        def movement(self, time, keys):
            for i in range(0.6):
                self.animales[i].mover(self, time, keys)
