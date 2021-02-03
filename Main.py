import pygame
from pygame.locals import *
import Data

WIDTH, HEIGHT = 1200, 800 #1200
SQ_SIZE =  16 
MAX_FPS = 1

def main():
    pygame.init()

    screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Jobs to Houses')
    screen.fill(pygame.Color('white'))

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

                #state.setSquare(squareSelected)

        drawState(screen)
        clock.tick(MAX_FPS)
        pygame.display.flip()

    
def drawState(screen):
    for r in range( HEIGHT // SQ_SIZE  ):
        for c in range( WIDTH // SQ_SIZE ):
            padding = 0.5
            margin = 4
            color = int( 255 - (0.2 * 255) )
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

            pygame.draw.rect(screen, getSquareColor(0), squareOuter)
            pygame.draw.rect(screen, pygame.Color( "white"), squareInner)

def getSquareColor(num):

    gray = int( 255 - (0.2 * 255) )
    
    if num == 0:
        return pygame.Color(gray, gray, gray)

main()