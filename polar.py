#polar coordinate grapher
#by parker sorenson
#11/12/17
import pygame, sys
from pygame.locals import *
import time
import numpy as np
import math
import random as rand

WINDOWWIDTH = 600
WINDOWHEIGHT = 400
WHITE = [255,255,255]
BLACK = [0,0,0]
LIGHTGREEN = [151,255,178]
LIGHTBLUE =[159,219,243]
DARKBLUE = [31,24,255]
INITRADIUS = 30
NUMOFCIRCLES = 5

def checkEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        INITRADIUS += 5
    elif keys[pygame.K_a]:
        INITRADIUS -= 5

def updateDots(alldots, forward):

    for circle in alldots:
        currentR = np.sqrt((circle[0][0])**(2) + (circle[0][1])**(2))    

        if forward:
            nextR = currentR + 5
        else:
            nextR = currentR - 4

        for n in range(len(circle)):
            circle[n][0] = nextR*math.sin(n)
            circle[n][1] = nextR*math.cos(n)

        #if too big
        if nextR > max(WINDOWWIDTH/2, WINDOWHEIGHT/2):
            for n in range(len(circle)):
                circle[n][0] = INITRADIUS*math.sin(n)
                circle[n][1] = INITRADIUS*math.cos(n)

def draw(screen, alldots, cColor, cCounter):

##    if cCounter == 0:
##        x = rand.randrange(WINDOWWIDTH)
##        y = rand.randrange(WINDOWHEIGHT)
##        for circle in alldots:
##            for dot in circle:
##                screen.set_at((x,y), cColor)
##    else:
    for circle in alldots:
        for dot in circle:
            x = int(WINDOWWIDTH/2 + dot[0])        
            y = int(WINDOWHEIGHT/2 + dot[1])
            screen.set_at((x,y), cColor)

def drawBackground(color):

    try:
        screen.fill(color)
    except TypeError:
        print(color)

#change colors
#colorcounter to loop from 0-255
#colorindex to choose between r,g, and b
def updateColors(bColor, cColor, cCounter, cIndex):

    #controlling values
    if bColor[cIndex] >= 255:        
        bColor[cIndex] = 0
        cIndex += 1
        if cIndex > 2:
            cIndex = 0 

    if cColor[cIndex] >= 254:
        cColor[cIndex] = 0
        cIndex += 1
        if cIndex > 2:
            cIndex = 0        

    #updating colors
    bColor[cIndex] += 1
    cColor[cIndex] += 2

    return bColor, cColor, cCounter, cIndex

def getDirection(forward, forwardCounter):
    if forwardCounter > 0:
        forward = True
        forwardCounter += 1
        if forwardCounter > 15:
            forwardCounter  = 0

    else:
        forward = False
        forwardCounter -= 1
        if forwardCounter < -4:
            forwardCounter = 1

    return forward, forwardCounter

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))    
    clock = pygame.time.Clock()
    fps = 60

    alldots = []
    
    for r in range(int(INITRADIUS)):
        if r % NUMOFCIRCLES == 0:
            circle = []
            for theta in range(720):
                circle.append([r*math.sin(theta),r*math.cos(theta)])
            alldots.append(circle)

    forward = True
    forwardCounter = 5
    
    bColor = LIGHTGREEN
    cColor = LIGHTBLUE
    cCounter = 0
    cIndex = 0
    while True:

        bColor, cColor, cCounter, cIndex = updateColors(bColor, cColor,
                                                    cCounter,
                                                    cIndex)
        forward, forwardCounter = getDirection(forward, forwardCounter)
        drawBackground(tuple(bColor))
        draw(screen, alldots, tuple(cColor), cCounter)
        updateDots(alldots,forward)
        checkEvents()                   
        pygame.display.update()
        clock.tick(fps)
if __name__=='__main__':
    main()
