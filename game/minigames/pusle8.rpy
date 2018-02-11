init python:

    #Imports que queramos hacer
    import random
    import pygame_sdl2 as pygame
    from pygame.locals import *

    WIDTH = config.screen_width
    HEIGHT = config.screen_height

    class Displayable(renpy.Displayable, img):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.white=White(Cell)
            self.original=img


    class Cell():
        """docstring for cell ."""
        def __init__(self, id, img, i, j, px, py):
            self.id = id
            self.image = img
            self.row = i
            self.col = j
            self.centerx = px
            self.centery = py
            self.side = None

        def draw(self, screen, st, at):
            pi = renpy.render(self.image, WIDTH, HEIGHT, st, at)
            if self.height is None:
                piw, self.height = pi.get_size()
            # renpy.render returns a Render object, which we can
            # blit to the Render we're making.
            screen.blit(pi, (int(self.centerx), int(self.centery)))

        def move(self, keys, board):
            if keys[K_d] and self.col<len(board[0])-1:
                self.col+=1
                self.centerx+=self.side
                board[self.row][self.col+1].col-=1
                board[self.row][self.col+1].centerx-=self.side

            if keys[K_a] and self.col>0:
                self.col-=1
                self.centerx-=self.side
                board[self.row][self.col-1].col+=1
                board[self.row][self.col-1].centerx+=self.side

            if keys[K_w] and self.row>0:
                self.row-=1
                self.centery-=self.side
                board[self.row-1][self.col].row+=1
                board[self.row-1][self.col].centery+=self.side

            if keys[K_s] and self.row<len(board[0])-1:
                self.row+=1
                self.centery+=self.side
                board[self.row+1][self.col].row-=1
                board[self.row+1][self.col].centery-=self.side

    class White(Cell):
        def __init__(self, id, path, i, j, px, py):
            super(White , self).__init__(id, path,i, j, px, py)


    class Img_cell(Cell):
        def __init__(self, id, img,i, j, px, py):
            super(Img_cell , self).__init__(id, img, i, j, px, py)


    class Pusle8(renpy.Displayable):

        #Debe sobreescribirse el constructor
        def __init__(self, path_img, num_div):
            self.image = path_img
            self.board = []
            self.num_div = num_div
            self.white = None

        def create_board(self):

            cuadrados = metodoMagico(self.image) #lo devuelve en una matriz para luego hacer los movimientos
            for row in range(0,num_div):
                self.board.append([None]*num_div)
                for column in range(0,num_div):
                    #ESE 100 NO ESTA BIEN, HAY QUE AVERIGUAR DONDE COMIENZA EL
                    #PUZLE Y SU PIXEL CENTRAL DE LA CASILLA SUPERIOR IZQUIERDA.
                    #ESO ES EL 100 DE PX Y PY
                    self.board[row][column] = Img_cell(row*num_div + column,
                                                       cuadrados[row][column],
                                                       row, column,
                                                       100*row, 100*column)

            white_cell = White(num_div**2-1, blanco_img, num_div-1, num_div-1, 100*num_div, 100*num_div)
            self.board[num_div-1][num_div-1] = white_cell
            self.white = white_cell

        def randomize(self):
            lista = {"a", "s", "w", "d"}
            i=0
            while(i<10)
                direction=random.choice(lista)
                if(not((last=="a" and direction=="d")or
                    (last=="s" and direction=="w")or
                    (last=="w" and direction=="s")or
                    (last=="d" and direction=="a"))):

                    cell.move(direction, board)
                    last=direction
                    i+=1

        def check(self, board):
            counter=0
            for col in board:
                for cell in col
                    if(cell.id=counter):
                        counter+=1
                        continue
                    else:
                        return False
            return True


        '''
        Renderiza el objeto en la escena.
        Heredado de renpy.Displayable

        width, side
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
