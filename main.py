import random
import sys
import pygame
from pygame.locals import *

Game_on = True

score = 0

screen_width = int(550)
screen_height = int(750)
screen = pygame.display.set_mode((screen_width,screen_height))   #for creating a GUI
fps = 32
pygame.display.set_caption('Flappy Bird by Arsalan Khan')

game_sprite = {}
game_sound= {}

bird_image = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\bird.png'   #creating a variable for storing a path of a image
Background = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\background.jpg'
pipe = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\pipe.png'
welcome_screen_image = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\welcome_screen.png'
gameOver_image = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\game_over.png'
tp = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\tp.jpeg'  #DELETE
play_again_img = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\play again.png'
start_game_img = 'C:\\Codes\\python\\Flappy Bird Game\\Sprites\\start game.png'

def Welcome_Screen() :
    while True :
        for event in pygame.event.get():
            if event.type == (QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif (event.type == KEYDOWN and event.key == K_SPACE) :
                return

            else :
                screen.blit(game_sprite['Background'] , (0,0))
                screen.blit(game_sprite['welcomescreen_image'] , (0,0))
                screen.blit(game_sprite['start_game'] , (70,450))

                button_coordinates = game_sprite['start_game'].get_rect()
                button_coordinates.topleft = (67,386)
                mouse_position = pygame.mouse.get_pos()
                mouse_click = False

                if (button_coordinates.collidepoint(mouse_position) ) :
                    if pygame.mouse.get_pressed()[0] == 1 and mouse_click == False :
                        mouse_click = True
                        return 

                pygame.display.update()
                fpsclock.tick(fps)

def Main_game(score) :

    score = 0
    bird_x_coordinate = screen_width/10
    bird_y_coordinate = (screen_height/2) - (game_sprite['Bird'].get_height())/2

    birdFallingVelocity = int(10)
    birdFlapped = int(-100)
    pipe_velocity_x = int(-4)
    flag = True

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    UpperPipes = [
        { 'x' : newPipe1[0]['x'] , 'y' : newPipe1[0]['y']} ,  #first upper pipe
        { 'x' : newPipe1[0]['x'] + (screen_width/1.3) , 'y' : newPipe2[0]['y']}  #second upper pipe
    ]

    LowerPipes = [
        { 'x' : newPipe1[0]['x'] , 'y' : newPipe1[1]['y']} ,   # first lower pipe
        { 'x' : newPipe1[0]['x'] + (screen_width/1.3) , 'y' : newPipe2[1]['y']}  #first lowerm pipe
    ]

    

    firstUpperPipe_x_coordinate = UpperPipes[0]['x']
    firstUpperPipe_y_coordinate = UpperPipes[0]['y']
    firstLowerPipes_x_coordinate = LowerPipes[0]['x']
    firstLowerPipes_y_coordinate = LowerPipes[0]['y']

    secondUpperPipe_x_coordinate = UpperPipes[1]['x']
    secondUpperPipe_y_coordinate = UpperPipes[1]['y']
    secondLowerPipes_x_coordinate = LowerPipes[1]['x']
    secondLowerPipes_y_coordinate = LowerPipes[1]['y']

    playerVelY = -9
    playerMaxVelY = 10

    playerAccY = 1
    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping

    while True :
        for event in pygame.event.get() :
            if event.type == (QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()  

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if bird_y_coordinate > 0:
                    game_sound['wing'].play()
                    playerVelY = playerFlapAccv
                    playerFlapped = True

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        
        playerHeight = game_sprite['Bird'].get_height()
        bird_y_coordinate = bird_y_coordinate + min(playerVelY, screen_height - bird_y_coordinate - playerHeight)

        #coding for moving pipes
        screen.blit(game_sprite['Background'] , (0,0))
        screen.blit(game_sprite['pipe'][0] , (firstUpperPipe_x_coordinate,firstUpperPipe_y_coordinate) )
        screen.blit(game_sprite['pipe'][1] , (firstLowerPipes_x_coordinate,firstLowerPipes_y_coordinate))
        screen.blit(game_sprite['pipe'][0] , (secondUpperPipe_x_coordinate,secondUpperPipe_y_coordinate) )
        screen.blit(game_sprite['pipe'][1] , (secondLowerPipes_x_coordinate,secondLowerPipes_y_coordinate) )
        firstUpperPipe_x_coordinate += pipe_velocity_x
        firstLowerPipes_x_coordinate += pipe_velocity_x
        secondUpperPipe_x_coordinate += pipe_velocity_x
        secondLowerPipes_x_coordinate += pipe_velocity_x
        if(firstUpperPipe_x_coordinate <= -(game_sprite['pipe'][0].get_width()) ):
            newPipe1.pop(0)
            newPipe1.pop(0)
            newPipe1 = getRandomPipe()
            #UpperPipes[0].pop()
            #LowerPipes[0].pop()
            
            firstUpperPipe_x_coordinate = newPipe1[0]['x'] + 100
            firstLowerPipes_x_coordinate = newPipe1[1]['x'] + 100
            firstUpperPipe_y_coordinate = newPipe1[0]['y']
            firstLowerPipes_y_coordinate = newPipe1[1]['y']

        if (secondLowerPipes_x_coordinate <= -(game_sprite['pipe'][0].get_width()) ) :
            newPipe2.pop(0)
            newPipe2.pop(0)
            i=2
            newPipe2 = getRandomPipe()
            secondUpperPipe_x_coordinate = newPipe2[0]['x'] + 100
            secondLowerPipes_x_coordinate = newPipe2[1]['x'] + 100
            secondUpperPipe_y_coordinate = newPipe2[0]['y']
            secondLowerPipes_y_coordinate = newPipe2[1]['y']
            i += 1

        #coding for moving bird
        screen.blit(game_sprite['Bird'] , (bird_x_coordinate , bird_y_coordinate))

        #for blitting the score 
        score_image = font.render(str(score) , True , pygame.Color('black')).convert_alpha()
        screen.blit(score_image , (270,100))

        #check for score
        pipeWidth = game_sprite['pipe'][0].get_width()
        #print(bird_x_coordinate,int(secondUpperPipe_x_coordinate) +  pipeWidth)
        if (bird_x_coordinate == firstUpperPipe_x_coordinate + pipeWidth + 1) :
            game_sound['score'].play()
            score = score + 1
        if (bird_x_coordinate == int(secondUpperPipe_x_coordinate) + pipeWidth + 1) :
            game_sound['score'].play()
            score += 1
            #added 1 to match the position of bird and coordinate of pipe 
            #print(bird_x_coordinate , firstUpperPipe_x_coordinate + pipeWidth + 1 ) enter this outside the if loop to check why I have added 1
        



        crashTest = isCollide(bird_x_coordinate,bird_y_coordinate,firstUpperPipe_x_coordinate,firstUpperPipe_y_coordinate,firstLowerPipes_x_coordinate,firstLowerPipes_y_coordinate,secondUpperPipe_x_coordinate,secondUpperPipe_y_coordinate,secondLowerPipes_x_coordinate,secondLowerPipes_y_coordinate)

        if crashTest == True :
            game_sound['hit'].play()
            return score

        pygame.display.update()
        fpsclock.tick(fps)

def isCollide(bird_x_coordinate,bird_y_coordinate,firstUpperPipe_x_coordinate,firstUpperPipe_y_coordinate,firstLowerPipes_x_coordinate,firstLowerPipes_y_coordinate,secondUpperPipe_x_coordinate,secondUpperPipe_y_coordinate,secondLowerPipes_x_coordinate,secondLowerPipes_y_coordinate) :
    
    birdWidth = game_sprite['Bird'].get_width() - 20
    birdHeight = game_sprite['Bird'].get_height() - 20  #-20 to avoid some space in bird image
    pipeWidth = game_sprite['pipe'][0].get_width()
    pipeHeight = game_sprite['pipe'][0].get_height()

    if bird_y_coordinate == screen_height - 100 or bird_y_coordinate == 0:
        return True
    
    #crash test for first upper and lower pipe both
    if ( (bird_x_coordinate + birdWidth > firstUpperPipe_x_coordinate) and (bird_x_coordinate < firstUpperPipe_x_coordinate + pipeWidth) ):
        if (bird_y_coordinate < firstUpperPipe_y_coordinate + pipeHeight) :  #crash test for upper pipe
            return True
        elif (bird_y_coordinate + birdHeight > firstLowerPipes_y_coordinate ) : #crash test for lower pipe
            return True 

    #crash test for second upper and lower pipe
    if ( (bird_x_coordinate + birdWidth > secondUpperPipe_x_coordinate) and (bird_x_coordinate < secondUpperPipe_x_coordinate + pipeWidth) ):
        if (bird_y_coordinate < secondUpperPipe_y_coordinate + pipeHeight) : #crash test for second upper pipe
            return True
        elif (bird_y_coordinate + birdHeight > secondLowerPipes_y_coordinate ) : #crash test for second lower pipe
            return True  

    return False
    
def getRandomPipe() : 
    pipHeight = game_sprite['pipe'][0].get_height()
    offset = int(250)

    Pipe_gap = int(250)

    y2 = offset + random.randrange(0,screen_height-offset) 

    pipe_x_cordinate = screen_width + int(10)

    pipe_y_coordinate = y2

    pipe = [
        { 'x' : pipe_x_cordinate , 'y' : -pipe_y_coordinate} ,  #for upper pipe
        { 'x' : pipe_x_cordinate , 'y' : (-pipe_y_coordinate + game_sprite['pipe'][0].get_height()) + Pipe_gap} #for lower pipe
    ]

    return pipe


def gameOver(score) :
    while True :
        screen.blit(game_sprite['Background'] , (0,0))
        screen.blit(game_sprite['Game_Over'] , (0,0))
        score_image = font.render(str(score) , True , pygame.Color('black')).convert_alpha()
        screen.blit(score_image , (400,260))
        screen.blit(game_sprite['play_again'] , (67,388))

        button_coordinates = game_sprite['play_again'].get_rect()
        button_coordinates.topleft = (67,386)
        mouse_position = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get() :
            if event.type == (QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif (event.type == KEYDOWN and event.key == K_SPACE) :
                Game_on = True
                return
        
        if (button_coordinates.collidepoint(mouse_position) ) :
            if pygame.mouse.get_pressed()[0] == 1 and mouse_click == False :
                mouse_click = True
                return 

        pygame.display.update()
        fpsclock.tick(fps)


if (__name__ == "__main__") :
    pygame.init()
    fpsclock = pygame.time.Clock()

    game_sprite['Bird'] = pygame.image.load(bird_image).convert_alpha() #importing images
    #convert_alpha blits(loads) the images quicker
    game_sprite['welcomescreen_image'] = pygame.image.load(welcome_screen_image) 
    game_sprite['Background'] = pygame.image.load(Background).convert_alpha()
    game_sprite['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha() , 180),
        pygame.image.load(pipe).convert_alpha()
    )
    game_sprite['Game_Over'] = pygame.image.load(gameOver_image).convert_alpha()
    game_sprite['tp'] = pygame.image.load(tp) #DEElete
    game_sprite['play_again'] = pygame.image.load(play_again_img).convert_alpha()
    game_sprite['start_game'] = pygame.image.load(start_game_img).convert_alpha()

    game_sound ['hit'] = pygame.mixer.Sound('C:\Codes\python\Flappy Bird Game\Sounds\\hit_sound.mpeg')
    game_sound ['score'] = pygame.mixer.Sound('C:\Codes\python\Flappy Bird Game\Sounds\\score_sound.mpeg')
    game_sound ['wing'] = pygame.mixer.Sound('C:\Codes\python\Flappy Bird Game\Sounds\\wing_sound.mpeg')

    font = pygame.font.SysFont('chalkduster.tff',150)

    
    Welcome_Screen()

    while Game_on == True :
        score = Main_game(score)
        gameOver(score)