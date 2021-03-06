# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Declare characters used by this game.
define h = Character('Herminda', color="#c8ffc8")
define p = Character('Pusles', color="#c8c8ff")
define k = Character('King', color='#c8c866')

#init python:
#    import text
#    """
#    Para poner los textos hay que poner:
#        "[text.<variable>]"
#    """

# The game starts here.

label start:

    #inventario
    python:
        ui.add(InventoryDisplayable())
        ui.interact(suppress_overlay=True, suppress_underlay=True)

#        if keys[K_i]:
#            showinventory = True
#            if keys[K_i]:
#                showinventory = False
#
    scene pub
    with fade

    show pusles at right
    with dissolve

    show herminda_simple at left
    with dissolve

#    p "[text.Flashback_PubConf_Pusles_1]"
#
#    show herminda_simple at left
#    with dissolve
#
#    h "[text.Flashback_PubConf_Hermilda_1]"
#
#    p "[text.Flashback_PubConf_Pusles_2]"
#
#    h "[text.Flashback_PubConf_Hermilda_2]"
#
#    p "[text.Flashback_PubConf_Pusles_3]"
#
#    h "[text.Flashback_PubConf_Hermilda_3]"
#
#    show pusles escupir at right
#
#    p "[text.Flashback_PubConf_Pusles_4]"
#
#    h "[text.Flashback_PubConf_Hermilda_4]"
#
#    p "[text.Flashback_PubConf_Pusles_5]"
#
#    p "[text.Flashback_PubConf_Pusles_6]"
#
#    h "[text.Flashback_PubConf_Hermilda_5]"
#
#    p "[text.Flashback_PubConf_Pusles_7]"
#
#label castle:
#
#    scene castle
#    with fade
#
#    show king at left
#    with dissolve
#    show pusles at right
#    with dissolve
#
#    p "[text.Flashback_Castle_Pusles_1]"
#
#    k "[text.Flashback_Castle_King_1]"
#
#    p "[text.Flashback_Castle_Pusles_2]"
#
#    k "[text.Flashback_Castle_King_2]"
#
#    p "[text.Flashback_Castle_Pusles_3]"
#
#    k "[text.Flashback_Castle_King_3]"
#
