# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    #python:
    #    ui.add(PongDisplayable())
    #    winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    python:
        ui.add(InventoryDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene bg washington
    show eileen vhappy

    window show None

    if winner == "enemy":

        e "I win!"

    else:

        e "You won! Congratulations."


label castle:

    scene castle
    with fade


    menu:
        e "Would you like to play again?"


    p "[text.Flashback_Castle_Pusles_1]"

    k "[text.Flashback_Castle_King_1]"

    p "[text.Flashback_Castle_Pusles_2]"

    k "[text.Flashback_Castle_King_2]"

    p "[text.Flashback_Castle_Pusles_3]"

    k "[text.Flashback_Castle_King_3]"
