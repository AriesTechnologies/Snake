
#Imports:
import pygame
from pygame.locals import *
import time
import random

#Start Pygame Commands:
PygameInit = pygame.init()

#Fonts
smallfont = pygame.font.SysFont ("comicsansms", 25)
mediumfont = pygame.font.SysFont ("comicsansms", 50)
largefont = pygame.font.SysFont ("comicsansms", 80)

#Colors:
black = (0,0,0)
darkgrey = (100,100,100)
grey = (150,150,150)
lightgrey = (200,200,200)
coffee = (170,110,60)
lightbrown = (190,120,50)
red = (255,0,0)
orange = (200,100,0)
OldGold = (197,179,88)
ElDoradoGold = (207,181,59)
yellow = (255,255,0)
darkgreen = (0,160,50)
green = (0,255,0)
greyblue = (115,140,190)
darkblue = (0,0,190)
navyblue = (0,0,150)
blue = (0,0,255)
teal = (0,255,255)
skyblue = (150,200,255)
violet = (255,0,255)
grape = (100,50,100)
darkpurple = (150,100,125)
purple = (180,0,255)
violet = (255,0,255)
white = (255,255,255)

#Variables:
display_w = 1280
display_h= 640
clock = pygame.time.Clock()
MenuFPS = 3
FPS = 20
PauseFPS = 3
block_Size = 20
Direction = "Right"

#WindowDisplay:
gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Snake 2.0")

icon = pygame.image.load('C:/Users/AtlasDisease/Pictures/Games/Snake/Icon.png')
pygame.display.set_icon(icon)
gameDisplay.fill(black)

#Images:
SnakeImg = pygame.image.load('C:/Users/AtlasDisease/Pictures/Games/Snake/SnakeHead.png')
AppleImg = pygame.image.load('C:/Users/AtlasDisease/Pictures/Games/Snake/Apple.png')
BirdieImg = pygame.image.load('C:/Users/AtlasDisease/Pictures/Games/Snake/Birdie.png')

#Definitions:
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            message_to_screen("Paused",
                                          ElDoradoGold,
                                          -100,
                                          size ="large")
            message_to_screen("Press Space to Continue or ESC to Quit",
                                          teal,
                                          25,
                                          size ="small")
            pygame.display.update()
            clock.tick(PauseFPS)
        
def Score(Score):
    text = smallfont.render("Score: "+str(Score), True, white)
    gameDisplay.blit(text, [0,0])
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                intro = False
                    
        gameDisplay.fill(black)
        message_to_screen("Snake 2.0",
                                      ElDoradoGold,
                                      -100,
                                      "large")
        message_to_screen("The objective of the game is to eat the neon blue powerups!",
                                        teal,
                                        -30)
        message_to_screen("Click to Start",
                                        teal,
                                        150)
        pygame.display.update()
        clock.tick(MenuFPS)
        
def Snake(block_Size , snakeList):

    if Direction == "Right":
        head = pygame.transform.rotate (SnakeImg, 270)
    if Direction == "Left":
        head = pygame.transform.rotate (SnakeImg, 90)
    if Direction == "Up":
        head = pygame.transform.rotate (SnakeImg, 0)
    if Direction == "Down":
        head = pygame.transform.rotate (SnakeImg, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList [-1][1]))      
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect (gameDisplay, ElDoradoGold, [XnY[0], XnY[1], block_Size, block_Size])

def Bird(block_Size , enemyList):
    head = pygame.transform.rotate (BirdieImg, 0)
    gameDisplay.blit(head, (enemyList[-1][0], enemyList [-1][1]))
    
    for XnY in enemyList[:-1]:
        pygame.draw.rect (gameDisplay, coffee, [XnY[0], XnY[1], block_Size, block_Size])
        
def text_objects (text, color, size):
    if size == "small":
        textSurface = smallfont.render (text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render (text, True, color)
    elif size == "large":
        textSurface = largefont.render (text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size ="small"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (display_w/2), (display_h/2)+y_displace
    gameDisplay.blit (textSurface, textRect)

#GameLoop:
def Gameloop():
    global Direction
    global Direction2
    Multiplayer = 0
    Direction ='Right'
    Direction2 = "Right"
    gameOver = False
    gameQuit = False
    lead_x = display_w/2
    lead_y = display_h/2
    leading_x = 20
    leading_y = 0
    PowerupX = round(random.randrange(0, display_w - block_Size)/20.0)*20.0
    PowerupY = round(random.randrange(0, display_h -block_Size)/20.0)*20.0                 
    EnemyX = 120
    EnemyY = 120
    enemyList = [ ]
    enemyHead = [ ]
    Leading_EnemyX = 20
    Leading_EnemyY = 0
    enemyL = 1
    snakeList = [ ]
    snakeHead = [ ]
    snakeL = 1
    Cursor_Pos = pygame.mouse.get_pos()

#   EventLoop:
    while not gameQuit:
        
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over!",
                                          red,
                                          y_displace=-50,
                                          size="large")
            message_to_screen("Click to Continue",
                                          red,
                                          y_displace=50,
                                          size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    gameQuit = True
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameOver = False
                    gameQuit= False
                    Gameloop()
                    continue

        for event in pygame.event.get():
            Cursor_Pos = pygame.mouse.get_pos()
            if gameOver == False:
                if Cursor_Pos[0] < 426:
                    Direction = "Left"
                    leading_x = -block_Size
                    leading_y = 0
                elif Cursor_Pos[0] > 852:
                    Direction = "Right"
                    leading_x = block_Size
                    leading_y = 0
                elif Cursor_Pos[1] < 350 and 852 > Cursor_Pos[0] > 426:
                    Direction = "Up"
                    leading_y = -block_Size
                    leading_x = 0
                elif Cursor_Pos[1] > 350 and 852 > Cursor_Pos[0] > 426:
                    Direction = "Down"
                    leading_y = block_Size
                    leading_x = 0
                if event.type == pygame.QUIT:
                    gameQuit = True
                    pygame.quit()
                    quit()
##                    elif event.key == pygame.K_p:
##                        pause()



    #               Boundaries:
        if  lead_y > display_h:
            lead_y = 0
            gameOver =  True
        elif lead_y < 0:
            lead_y = display_h-10
            gameOver =  True
        elif lead_x > display_w:
            lead_x = 0
            gameOver =  True
        elif lead_x < 0:
            lead_x = display_w-10
            gameOver =  True
        elif EnemyX > display_w:
            gameOver = True
        elif EnemyX < 0:
            gameOver = True
        elif EnemyY > display_h:
            gameOver = True
        elif EnemyY < 0:
            gameOver = True

#       Graphic Updates:
        lead_x += leading_x
        lead_y += leading_y
        if Multiplayer == 1:
            EnemyX += Leading_EnemyX
            EnemyY += Leading_EnemyY
            gameDisplay.blit(BirdieImg, (EnemyX, EnemyY))
        gameDisplay.fill(black)
        Score(snakeL-1)
        gameDisplay.blit(AppleImg, (PowerupX, PowerupY))
        snakeHead = [ ]
        snakeHead.append (lead_x)
        snakeHead.append (lead_y)
        snakeList.append (snakeHead)
        enemyHead = [ ]
        enemyHead.append (EnemyX)
        enemyHead.append (EnemyY)
        enemyList.append (enemyHead)
        
        #SnakeRules:
        if len(snakeList) > snakeL:
            del snakeList [0]
            for eachSegment in snakeList [-1]:
                if eachSegment == snakeHead:
                    gameOver == True
                    gameQuit == True
                
        Snake(block_Size, snakeList)
        gameDisplay.blit(BirdieImg, (EnemyX, EnemyY))
        pygame.display.update()

#       Powerup/Enemy Movement:
        if lead_x == PowerupX and lead_x == PowerupX and lead_y == PowerupY and lead_y == PowerupY:
            PowerupX = round(random.randrange(0, display_w - (block_Size*2))/20.0)*20.0
            PowerupY = round(random.randrange(0, display_h - (block_Size*2))/20.0)*20.0
            if Multiplayer == 0:
                PowerupX = round(random.randrange(0, display_w - block_Size)/20.0)*20.0
                PowerupY = round(random.randrange(0, display_h - block_Size)/20.0)*20.0
                EnemyX = round(random.randrange(0, display_w - block_Size)/20.0)*20.0
                EnemyY = round(random.randrange(0, display_h - block_Size)/20.0)*20.0
                snakeL += 1
        if EnemyX == PowerupX and EnemyY == PowerupY:
            enemyL += 1
        pygame.display.update()
            
#       Enemy Detection:
        if lead_x == EnemyX and lead_y == EnemyY:
            gameOver = True
            gameQuit = False

#       Frames Per Second:
        clock.tick(FPS)

#   Quit:
    pygame.quit()
    quit()

#EndingGameloop:
game_intro()
Gameloop()
