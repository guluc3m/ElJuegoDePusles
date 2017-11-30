# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Declare characters used by this game.
define h = Character('Herminda', color="#c8ffc8")
define p = Character('Pusles', color="#c8c8ff")

init python:
    import text
    """
    Para poner los textos hay que poner:
        "[text.<variable>]"
    """

# The game starts here.

label start:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene pub
    with fade

    show pusles at right
    with dissolve

    p "[text.Flashback_PubConf_Pusles1]"

    show herminda_simple at left
    with dissolve

    h "[text.Flashback_PubConf_Hermilda1]"

    p "[text.Flashback_PubConf_Pusles2]"

    h "[text.Flashback_PubConf_Hermilda2]"

    p "[text.Flashback_PubConf_Pusles3]"

    h "[text.Flashback_PubConf_Hermilda3]"

    show pusles escupir at right

    p "[text.Flashback_PubConf_Pusles4]"

    h "[text.Flashback_PubConf_Hermilda4]"

    p "[text.Flashback_PubConf_Pusles5]"

    p "[text.Flashback_PubConf_Pusles6]"

    h "[text.Flashback_PubConf_Hermilda5]"

    p "[text.Flashback_PubConf_Pusles7]"

