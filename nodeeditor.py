#Iteration 1: load a window and set it's caption
#Iteration 2: escape key quits, Track the Mouse and display debug info
#Iteration 3: draw box and move with mouse
#Iteration 4: refactor debug system
import yaml
import pygame

def debugMsg(msg):
    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'msg':str(msg)}))
    
def main():
# Load window
    #Set Window Size and graphical context
    pygame.init()
    screen = pygame.display.set_mode((800,600),pygame.RESIZABLE,0)
    #set window title
    pygame.display.set_caption("Node Editor")
    #load media
    box = pygame.Surface((200,100))
    box_rect = box.fill((100,100,200))
    boxposx = 100
    boxposy = 100
    
    cursor = pygame.Surface((5,5))
    cursor_rect = cursor.fill((200,200,100))
    cursor_pos = (0,0)
    cursor_click = (0,0,0)
    cursor_rel = (0,0)
    
    debug_font = debug_font = pygame.font.Font(None,20)
    debug_color = (200,200,200)
    debug_posx = 5
    debug_posy = 5
    #get initial state information
    quit = False
    
#main loop
    while quit == False:
        #handle events
        for event in pygame.event.get():
            #when someone presses the exit button
            if event.type == pygame.QUIT:
                quit = True
            #handle keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
            #handle mouse input
            if event.type == pygame.MOUSEMOTION:
                #Track the Mouse
                cursor_click = event.buttons
                cursor_pos = event.pos
                cursor_rel = event.rel
                if event.buttons == (1,0,0) and cursor_rect.colliderect(box_rect):
                    movex, movey = cursor_rel
                    boxposx = movex+boxposx
                    boxposy = movey+boxposy
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_click = event.button
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            #display debug info
            if event.type == pygame.USEREVENT:
                debug_msg = event.msg
                debug_render = debug_font.render(debug_msg,True,debug_color)
                screen.blit(debug_render,(debug_posx,debug_posy))
                debug_posy = debug_posy+15

        debug_posy = 5
        
        debugMsg(cursor_pos)
        debugMsg(box_rect)
        debugMsg(cursor_rect)
        #update display
        box_rect = screen.blit(box,(boxposx,boxposy))
        cursor_rect = screen.blit(cursor,cursor_pos)
        pygame.display.flip()
        screen.fill((0,0,0))

main()
