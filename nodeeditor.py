import pygame

#global constants
RGB_DARKGREY=(100,100,100)
RGB_MEDIUMGRAY=(150,150,150)

def draw_link(nodeOut=None, nodeIn=None):
    """
    draw_link(nodeOut,nodeIn)

    draws a links between two nodes

    default nodeOut = None
    default nodeIn = None
    """
    #get pygame display surface
    display = pygame.display.get_surface()
    #get position of output on nodeOut
    rectOut = nodeOut.get_rect()
    #get position of input on nodeIn
    rectIn = nodeIn.get_rect()
    #draw bezier between input and output
    #return surface of bezier
    return link
def draw_node(size=(100,100)):
    """
    draw_node(size=(width,height))

    draw a node with input and output points
    
    default width = 100
    default height = 100
    """
    #create a new surface
    node=pygame.Surface(size)
    #create a border of dark grey
    node.fill((100,100,100))
    #fill with medium grey
    node.fill((150,150,150),(1,1,98,98))
    #draw input 
    pygame.draw.circle(node,(100,100,100),(0,20),5)
    #draw output
    pygame.draw.circle(node,(100,100,100),(100,80),5)

    return node

def main():
    """Initializes, runs the main/master loop"""

    #Initialize Pygame
    pygame.init()

    #Initial screen setup
    display=pygame.display.set_mode((800,600))
    
    #initial variable setup
    quit=False

    #main loop
    while quit==False:
        #wait for a key then exit
        if pygame.event.peek(pygame.KEYDOWN):
            quit=True
        #draw box in window
        node1=draw_node()
        node2=draw_node()
        display.blit(node1,(20,20))
        display.blit(node2,(100,200))
        #keep screen updated
        pygame.display.flip()
main()

#DONE
#step one, show window
#step two, draw box in window
#step three, draw 2 boxes in window
#step four, draw input and output sections on boxes

#TODO
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

