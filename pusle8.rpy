init python:

    #Imports que queramos hacer
    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    class Cell():
        """docstring for cell ."""
        def __init__(self, id, path, i, j, px, py):
            self.id = id
            self.image = Image(path)
            self.row = i
            self.col = j
            self.centerx = px
            self.centery = py
            self.height = None

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            if self.height is None:
                piw, self.height = pi.get_size()
            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))

        def move(self, keys, board):
            if keys[K_d] and self.col<len(board[0])-1:

            if keys[K_a] and self.col<len(board[0])-1:

            if keys[K_w] and self.col<len(board[0])-1:

            if keys[K_s] and self.col<len(board[0])-1:



    class White(Cell):
        def __init__(self, id, path, i, j, px, py):
            super(White , self).__init__(id, path,i, j, px, py)


    class Img_cell(Cell):
        def __init__(self, id, path,i, j, px, py):
            super(Img_cell , self).__init__(id, path, i, j, px, py)



    class Pusle8(renpy.Displayable):

        #Debe sobreescribirse el constructor
        def __init__(self, image, **kwargs):
            pass

        '''
        Renderiza el objeto en la escena.
        Heredado de renpy.Displayable

        width, height
            The amount of space available to this displayable, in pixels.
        st
            A float, the shown timebase, in seconds. The shown timebase
            begins when this displayable is first shown on the screen.
        at
            A float, the animation timebase, in seconds. The animation timebase begins when
            an image with the same tag was shown, without being hidden.
            (When the displayable is shown without a tag, this is the same as
                the shown timebase.) '''
        def render(self, width, height, st, at):
            pass


        '''
        ev
            An event object
        x, y
            The x and y coordinates of the event, relative to the upper-left
            corner of the displayable. These should be used in preference to
            position information found in the pygame event objects.
        st
            A float, the shown timebase, in seconds.

        An event is generated at the start of each interaction, and renpy.timeout()
        can be used to cause another event to occur.'''
        def event(self, ev, x, y, st):
            pass

        '''
        Similar a update de pygame'''
        def per_interact(self):
            pass

        '''
        Devuelve la lista de hijos '''
        def visit(self):
            return [ self.child ]
