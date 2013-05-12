#Iteration 1: load a window and set it's caption
#Iteration 2: escape key quits, Track the Mouse and display debug info
import yaml
import pygame

def main():
# Load window
    #Set Window Size and graphical context
    pygame.init()
    screen = pygame.display.set_mode((800,600),pygame.RESIZABLE,0)
    #set window title
    pygame.display.set_caption("Node Editor")
    #load media
    
    #draw buttons
    #draw canvas
    
    #get initial state information
    quit = False
    #test if opening file or new file
    #test if opening medium or new medium
#main loop
    while quit == False:
        #set escape sequence
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit = True
        
        #Track the Mouse
        cursor=pygame.mouse.get_pos()
        #display debug info
        debug_font = pygame.font.Font(None,20)
        debug_cursorposition = debug_font.render(str(cursor),True,(200,200,200))
        debug_pos = (20,20)
        screen.blit(debug_cursorposition,debug_pos)
        pygame.display.flip()
        screen.fill((0,0,0))
#Manipulate Nodes
    #add nodes
    #remove nodes and connectors
    #disconnect nodes from connectors
    #move nodes and connectors
    #focus on node
    #update node info

main()
    