import pygame
def main():
"""Initializes, runs the main/master loop"""

    #Initialize Pygame
    pygame.init()

    #Initial screen setup
    pygame.display.set_mode((800,600))
    
    #initial variable setup
    quit=False

    #main loop
    while quit==False:
        #wait for a key then exit
        if pygame.event.peek(pygame.KEYDOWN):
            quit=True
main()

#step one, show window
#step two, draw box in window
#step three, draw 2 boxes in window
#step four, draw input and output sections on boxes
#step five, draw line between input and output sections
#step six, be able to move boxes around while keeping line attached.
#step seven, add buttons to boxes
#step eight, be able to add boxes
#step nine, be able to remove boxes
#step ten, be able to connect all the boxes
#step eleven, be able to store layout and connections of boxes
#step twelve, add "meanings" to boxes
#step thirteen, parse layout of boxes and execute meanings
#step fourteen, add textboxes
#step fifteen, add color pickers
#step sixteen, add visualization tools
#step seventeen, add language parsers

