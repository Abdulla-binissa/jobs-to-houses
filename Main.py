import pygame
from pygame.locals import *
import Data

SQ_SIZE =  16 
MAX_FPS = 15

def main():
    WIDTH, HEIGHT = 1200, 800
    pygame.init()

    screen = pygame.display.set_mode(( WIDTH, HEIGHT ), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pygame.display.set_caption('Jobs to Houses')
    screen.fill(pygame.Color('white'))
    state = Data.State()

    #state.add((HEIGHT// SQ_SIZE // 2,WIDTH// SQ_SIZE // 2))
    state.add( (0, 0) )

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = (location[0] - WIDTH / 2) // SQ_SIZE 
                row = (location[1] - HEIGHT / 2) // SQ_SIZE 
                cellSelected = (row, col)

                state.cellClicked(cellSelected)

            elif event.type == pygame.VIDEORESIZE:
                screen.fill(pygame.Color('white'))
                HEIGHT = screen.get_height()
                WIDTH = screen.get_width()
                
        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

    
def drawState(screen, state):
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()

    left = (WIDTH / SQ_SIZE / 2) - (WIDTH / SQ_SIZE)
    right = (WIDTH / SQ_SIZE / 2 )
    top = (HEIGHT / SQ_SIZE / 2 ) - (HEIGHT / SQ_SIZE)
    bottom = (HEIGHT / SQ_SIZE / 2)

    for r in range( int(top) -1, int(bottom) +1):
        for c in range( int(left) -1, int(right) +1):

            padding, margin = 0.5, 4
            squareOuter = pygame.Rect(
                (right+c)*SQ_SIZE + padding, 
                (bottom+r)*SQ_SIZE + padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareInner = pygame.Rect(
                (right+c)*SQ_SIZE + padding + margin, 
                (bottom+r)*SQ_SIZE + padding + margin, 
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