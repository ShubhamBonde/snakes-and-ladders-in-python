import pygame
import time
import random
import math
from pygame import mixer

pygame.init()
game_state = 'ready'
screen = pygame.display.set_mode((1000,700))
# VARIABLES
Playing = True
dice = 0

# IMAGES
board = pygame.image.load('.\images\gameboard.png')
# PLAYER IMAGES:
player1 = pygame.image.load('.\images\player\Player_1.png')

#position:
player1X = 0

coordinates = 1
oldLocation = 1
counter = 1

# RESOLUTION OF THE TILE
TILE_RES = 70
# TILE AND ROW:

tileNO = (player1X/TILE_RES)+1
P1X_cal = 0
INT_TILE=1


#FONTS:
dicetxt = pygame.font.Font('./fonts/josephin.ttf',20)


# DICTIONARY FOR THE PLAYER LOCATIONS:
playerLoc = {
    "1" :(0,630),"2":(70,630),"3":(140,630),"4":(210,630),"5":(280,630),"6":(350,630),"7":(420,630),"8":(490,630),"9":(560,630),"10":(630,630),
    "11":(630,560),"12":(560,560),"13":(490,560),"14":(420,560),"15":(350,560),"16":(280,560),"17":(210,560),"18":(140,560),"19":(70,560),"20":(0,560),
    "21":(0,490),"22":(70,490),"23":(140,490),"24":(210,490),"25":(280,490),"26":(350,490),"27":(420,490),"28":(490,490),"29":(560,490),"30":(630,490),
    "31":(630,420),"32":(560,420),"33":(490,420),"34":(420,420),"35":(350,420),"36":(280,420),"37":(210,420),"38":(140,420),"39":(70,420),"40":(0,420),
    "41":(0,350), "42":(70,350), "43":(140,350), "44":(210,350), "45":(280,350), "46":(350,350), "47":(420,350), "48":(490,350), "49":(560,350), "50":(630,350),
    "51":(630,280),"52":(560,280),"53":(490,280),"54":(420,280),"55":(350,280),"56":(280,280),"57":(210,280),"58":(140,280),"59":(70,280),"60":(0,280),
    "61":(0,210), "62":(70,210), "63":(140,210), "64":(210,210), "65":(280,210), "66":(350,210), "67":(420,210), "68":(490,210), "69":(560,210), "70":(630,210),
    "71":(630,140),"72":(560,140),"73":(490,140),"74":(420,140),"75":(350,140),"76":(280,140),"77":(210,140),"78":(140,140),"79":(70,140),"80":(0,140),
    "81":(0,70), "82":(70,70), "83":(140,70), "84":(210,70), "85":(280,70), "86":(350,70), "87":(420,70), "88":(490,70), "89":(560,70), "90":(630,70),
    "91":(630,0),"92":(560,0),"93":(490,0),"94":(420,0),"95":(350,0),"96":(280,0),"97":(210,0),"98":(140,0),"99":(70,0),"100":(0,0), "101":(0,0),"102":(0,0),"103":(0,0),
    "104":(0,0),"105":(0,0),"106":(0,0)
}





while Playing:
    
    dicetxt_msg = dicetxt.render(f"Dice Rolled:{dice}",True,(255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        
        key = pygame.key.get_pressed()
        if key:
            game_state = 'ready'
        if game_state =='ready':
            if key[pygame.K_SPACE]:
                DiceRoll = mixer.Sound('.\sounds\DiceRoll.wav')
                dice = random.randint(1,6) #Randomly will get 1 to 6 (anything)
                print(f"Dice rolled:{dice}")
                DiceRoll.play()
                oldLocation = coordinates
                print(f"Old location:{oldLocation}")
                coordinates += dice
                counter += dice
                print(f"Counter{counter}")
                print(f"100-coordinates: {100-counter}")
                if coordinates>100:
                    coordinates= oldLocation
                
                """So here is the Proglem: 
                   The co-ordinates is crossing the mark of 100 and that is not desirable
                   that is giving the 'key-Error' Now How do I stop it?
                   I've tried various combinations of if and else but it didn't worked at all
                   the co-ordinates keeps crossing the mark of 100"""
                
                

                    


                print(f"Current Tile:{coordinates}")
                

                
                # USED TO BE VERY IMPORTANT LINES:
                # tileNO = (coordinates)+1
                # INT_TILE = int(tileNO)
                # print(f"Current tile:{INT_TILE}")
                # last_tile = INT_TILE-dice
                # print(f"Last tile:{last_tile}")
                # Tile_to_win = (100-INT_TILE)
                # print(f"Tile to win:{Tile_to_win}")
                
                    
                    
                

                
                




                
                             
                
                

                
                game_state ='not ready'
                
                
                print("-------------------------------------------------------------")



                    
                
                
                
                    
            
            
            
    
    screen.fill((0,10,50))
    screen.blit(board,(0,0))
    
    screen.blit(player1,playerLoc[f"{coordinates}"]) #Tuple of: (co_ordinate X, co_ordinate Y)
    
       

    screen.blit(dicetxt_msg,(720,50))
    

    
    pygame.display.update()
