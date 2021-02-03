import pygame
from pygame.locals import *
import Data

WIDTH, HEIGHT = 1200, 800 #1200
SQ_SIZE =  16 
MAX_FPS = 15

def main():
    pygame.init()

    screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Jobs to Houses')
    screen.fill(pygame.Color('white'))
    state = Data.State()

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                squareSelected = (row, col)

                state.setCell(squareSelected)

        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

    
def drawState(screen, state):
    for r in range( HEIGHT // SQ_SIZE  ):
        for c in range( WIDTH // SQ_SIZE ):
            padding, margin = 0.5, 4
            squareOuter = pygame.Rect(
                c*SQ_SIZE + padding, 
                r*SQ_SIZE + padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareInner = pygame.Rect(
                c*SQ_SIZE + padding + margin, 
                r*SQ_SIZE + padding + margin, 
                SQ_SIZE - 2*padding - 2*margin, 
                SQ_SIZE - 2*padding - 2*margin)
            color = state.getCellValue((r,c))

            pygame.draw.rect(screen, getSquareColor(color), squareOuter)
            pygame.draw.rect(screen, pygame.Color( "white"), squareInner)

# Uses cell value to determine strength of color
# Green(Values 0 to 1) Red(values -1 to 0) Gray(0)
def getSquareColor(value):
    alpha = int( 255 - abs(value)*255  )
    if value > 0:
        r = int( (11 + alpha)/2 )
        g = int( (156 + alpha)/2 )
        b = int( (49 + alpha)/2 )
        return pygame.Color(r, g, b)
    elif value < 0:
        r = 255
        g = b = int( (0 + alpha)/2 )
        return pygame.Color(r, g, b) 
    else:
        return pygame.Color(200, 200, 200)
        
                

main()