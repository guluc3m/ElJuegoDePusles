# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start2:

    window hide None

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene bg washington
    show eileen vhappy

    window show None

    if winner == "enemy":

        e "I win!"

    else:

        e "You won! Congratulations."

    show eileen happy

    menu:
        e "Would you like to play again?"

        "Sure.":
            jump start
        "No thanks.":
            pass