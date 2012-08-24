import pygame
def main():
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
