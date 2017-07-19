init python:

    #Imports que queramos hacer

    class Name(renpy.Displayable):

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