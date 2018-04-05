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
        def __init__(self, elem):
            self.elem=elem
            #El snake part encapsulado
            self.next=None
                #a priori self.next es None y ya se ira llenando conforme coma

        def move(self, direction):
        	if(direction=="r"):self.elem.x+=1
        	if(direction=="u"):self.elem.y+=1
        	if(direction=="d"):self.elem.y-=1
        	if(direction=="l"):self.elem.x-=1

    class snake_complete():
        def __init__(self):
            self.first=None#Cuando inicie el juego hay que añadir un first aqui
            #self.first es la cabesa
            self.last=first
            self.length=1

        def addLast(self, elem):
        	SNode=node(elem)
        	self.last.next=SNode
        	last=SNode

        def move(self, direction):
        	moved=false
        	while(not moved):
        		nodeIt=self.first
        		nodeIt.move(direction)
        		nodeIt=nodeIt.next
        		if(nodeIt.next==None):
        			moved=true

        def eat(self, food):
        	elem=snake_part(food.x, food.y, "blender/juegosbasura/untitled.xcf")
        	#recuerda cambiar el archivo que no esta para nada bien
        	self.addLast(elem)
        	#tengo que hacer algo tipo move pero que el ultimo no se mueva



    class food():
        def __init__(self, x, y, image):
            self.x=x
            self.y=y
            self.image=image

        def reSpawn(self):
        	xtemp=self.x
        	ytemp=self.y
        	while(xtemp!=self.x and ytemp!=self.y):
        		self.x=(int)random()*WIDTH
        		self.y=(int)random()*height
       	#	self.draw()



    class juego():
        pass
