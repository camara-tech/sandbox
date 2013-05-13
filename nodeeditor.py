#Iteration 1: load a window and set it's caption
#Iteration 2: escape key quits, Track the Mouse and display debug info
#Iteration 3: draw box and move with mouse
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
    box = pygame.Surface((200,100))
    box_rect = box.fill((100,100,200))
    boxposx = 100
    boxposy = 100
    
    cursor = pygame.Surface((5,5))
    cursor_rect = cursor.fill((200,200,100))
    cursor_pos = (0,0)
    cursor_click = (0,0,0)
    cursor_rel = (0,0)
    #draw buttons
    #draw canvas
    
    #get initial state information
    quit = False
    #test if opening file or new file
    #test if opening medium or new medium
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
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        
        
        #display debug info
        debug_font = pygame.font.Font(None,20)
        debug_cursorposition = debug_font.render(str(cursor_pos),True,(200,200,200))
        debug_cursorclicks=debug_font.render(str(box_rect),True,(200,200,200))
        debug_cursorrel=debug_font.render(str(cursor_rect),True,(200,200,200))
        debug_pos1 = (5,5)
        debug_pos2 = (5,20)
        debug_pos3 = (5,35)
        #update display
        box_rect = screen.blit(box,(boxposx,boxposy))
        cursor_rect = screen.blit(cursor,cursor_pos)
        screen.blit(debug_cursorposition,debug_pos1)
        screen.blit(debug_cursorclicks,debug_pos2)
        screen.blit(debug_cursorrel,debug_pos3)
        pygame.display.flip()
        screen.fill((0,0,0))

main()
    