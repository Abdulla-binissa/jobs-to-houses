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
    screen.set_alpha(128)

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
                cellSelected = (row, col)

                state.setCell(cellSelected)

            

        drawGrid(screen)
        drawCells(screen, state)

        clock.tick(MAX_FPS)
        pygame.display.flip()

    
def drawGrid(screen):
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

            pygame.draw.rect(screen, pygame.Color(200, 200, 200), squareOuter)
            pygame.draw.rect(screen, pygame.Color( "white"), squareInner)


def drawCells(screen, state):
    surface = pygame.Surface( (HEIGHT, WIDTH) )
    surface.fill('white')
    surface.set_alpha(0)
    
    for r in range( HEIGHT // SQ_SIZE  ):
        for c in range( WIDTH // SQ_SIZE ):
            cellValue = state.getCellValue((r, c))
            cell = pygame.Surface( (SQ_SIZE, SQ_SIZE) )
            cell.fill('white')

            if cellValue < 0:
                cellColor = pygame.Color(255, 0, 0) 
                alpha = int( abs(cellValue)*255 )
            elif cellValue > 0:
                cellColor = pygame.Color(11, 156, 49)
                alpha = int( abs(cellValue)*255 )
            else:
                cellColor = pygame.Color(200, 200, 200)
                alpha = 0
                
            cell.set_alpha( alpha )

            padding, margin = 0.5, 4
            squareOuter = pygame.Rect(
                padding, 
                padding, 
                SQ_SIZE - 2*padding, 
                SQ_SIZE - 2*padding)
            squareInner = pygame.Rect(
                padding + margin, 
                padding + margin, 
                SQ_SIZE - 2*padding - 2*margin, 
                SQ_SIZE - 2*padding - 2*margin)

            pygame.draw.rect(cell, cellColor, squareOuter)
            pygame.draw.rect(cell, pygame.Color( "white"), squareInner)
            screen.blit(cell, (c*SQ_SIZE,r*SQ_SIZE)) 

    #screen.blit(surface, (0,0))

            

main()