init python:

    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    # This draws a paddle, and checks for bounces.
    class Pala():
        def __init__(self, px):
            self.image = Image("pong/pala.png")
            self.centerx = px
            self.centery = HEIGHT/2
            self.height = None
            self.speed = 450

        def mover(self, time, keys):
            if self.centery >= 0:
                # Flechita hacia arriba
                if keys[K_w]:
                    self.centery -= self.speed * time
            if self.centery+self.height <= HEIGHT:
                # Flechita hacia abajo
                if keys[K_s]:
                    self.centery += self.speed * time

        def ia(self, time, ball):
            if ball.speed[0] >= 0 and ball.centerx >= WIDTH/2:
                if self.centery < ball.centery:
                    self.centery += self.speed * time
                if self.centery > ball.centery:
                    self.centery -= self.speed * time

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            if self.height is None:
                piw, self.height = pi.get_size()
            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))

    class Bola():
        def __init__(self):
            self.image = Image("pong/ball.png")
            #Se coloca la peloca en el centro de la ventana
            self.centerx = WIDTH/2
            self.centery = HEIGHT/2
            #Velocidad en el eje X, eje Y
            self.speed = [500, -500]

        def reset(self):
            self.centerx = WIDTH / 2
            self.centery = HEIGHT / 2
            if random.random() > 0.45: 
                mult1 = -1
                mult2 = 1
            else:
                mult1 = 1
                mult2 = -1
            self.speed = [mult1*500, mult2*500]

        def update(self, time, pala_jug, pala_cpu, puntos):
            # Espacio = V * T
            self.centerx += self.speed[0] * time
            self.centery += self.speed[1] * time

            #print(self.speed[0] * time)
            #print(self.speed[1] * time)
            #print(self.centerx)

            if self.centerx <= 15:
                puntos[1] += 1
                #print("valores jug -----------------------")
                #print(int(self.centerx) == int(pala_jug.centerx))
                #print(self.centery >= pala_jug.centery)
                #print(self.centery <= pala_jug.centery + pala_jug.height)
                #print(int(self.centerx))
                #print(int(pala_jug.centerx))
                #print(self.centery)
                #print(pala_jug.centery + pala_jug.height)
                self.reset()
            if self.centerx >= WIDTH-15:
                puntos[0] += 1
                #print("valores cpu -----------------------")
                #print(int(self.centerx) == int(pala_cpu.centerx))
                #print(self.centery >= pala_cpu.centery)
                #print(self.centery <= pala_cpu.centery + pala_cpu.height)
                #print(int(self.centerx))
                #print(int(pala_cpu.centerx))
                #print(self.centery)
                #print(pala_cpu.centery + pala_cpu.height)
                self.reset()

            # Rebota arriba o abajo
            if self.centery >= HEIGHT or \
                self.centery <= 0:
                self.speed[1] = -self.speed[1]
                self.centery += self.speed[1] * time

            # Rebota pala
            if (int(self.centerx) <= int(pala_jug.centerx+5) and \
                self.centery >= pala_jug.centery and \
                self.centery <= pala_jug.centery + pala_jug.height) or \
                (int(self.centerx) >= int(pala_cpu.centerx-5) and \
                self.centery >= pala_cpu.centery and \
                self.centery <= pala_cpu.centery + pala_cpu.height):

                self.speed[0] = -self.speed[0]
                self.centerx += self.speed[0] * time

            return puntos

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)

            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))


    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            renpy.Displayable.__init__(self)

            #Elementos a mostrar
            ''' Carga de la pelotica '''
            self.bola = Bola()

            ''' Carga jugador (a 30px de la izq)'''
            self.pala_jug = Pala(30)

            ''' Carga cou (a 30px a la drch)'''
            self.pala_cpu = Pala(WIDTH - 30)

            self.player = Text(_("Pepe"), size=36)
            self.enemy = Text(_("Enemy"), size=36)
            self.start = Text(_("Click to Begin"), size=40)

            self.puntos = [0,0]
            #Para calcular tiempos
            self.oldst = None
            self.winner = False
            self.stuck = True

        def render(self, width, height, st, at):
            # Similar al screen de pygame
            r = renpy.Render(width, height)

            # Para poder saber el tiempo
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st
            if not self.stuck:
                # Actualiza bola
                self.puntos = self.bola.update(dtime, self.pala_jug, \
                    self.pala_cpu, self.puntos)

                # Actualiza pala CPU
                self.pala_cpu.ia(dtime, self.bola)

            # Dibuja el nombre del jugador
            player = renpy.render(self.player, WIDTH, HEIGHT, st, at)
            r.blit(player, (20, 25))

            # Dibuja el nombre del enemigo
            enemy = renpy.render(self.enemy, WIDTH, HEIGHT, st, at)
            ew, eh = enemy.get_size()
            r.blit(enemy, (790 - ew, 25))

            # Dibuja puntos jugador
            puntos_pj = renpy.render(Text(str(self.puntos[0]), size=36), WIDTH, HEIGHT, st, at)
            r.blit(puntos_pj, (WIDTH/2-100, 25))

            # Dibuja puntos enemigo
            puntos_enemy = renpy.render(Text(str(self.puntos[1]), size=36), WIDTH, HEIGHT, st, at)
            r.blit(puntos_enemy, (WIDTH-100, 25))

            # Show the "Click to Begin" label.
            if self.stuck:
                ctb = renpy.render(self.start, WIDTH, HEIGHT, st, at)
                ctbw, ctbh = ctb.get_size()
                r.blit(ctb, (WIDTH/2-ctbw/2, HEIGHT/2))


            # Check for a winner.
            if self.puntos[0] >= 3:
                self.winner = "player"
                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.puntos[1] >= 3:
                self.winner = "enemy"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            self.bola.draw(r, st, at)
            self.pala_jug.draw(r, st, at)
            self.pala_cpu.draw(r, st, at)

            # Return the Render object.
            return r

        def event(self, ev, x, y, st):

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

            dtime = st - self.oldst
            # Actualiza pala jugador
            self.pala_jug.mover(dtime, pygame.key.get_pressed())


            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

        def visit(self):
            return [self.player, self.enemy, self.start]

