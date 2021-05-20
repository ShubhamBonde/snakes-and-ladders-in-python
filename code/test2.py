import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,700))
running = True
board = pygame.image.load('.\images\gameboard.png')
player1 = pygame.image.load('.\images\player\player_1.png')

#player1 posi
player1X = 0
player1Y = 630
state = 'ready'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key:
            state = 'ready'
        if state == 'ready':
            if key[pygame.K_SPACE]:
                dice = random.randint(1,6)
                # Rewrite an alogorithm for movement alon rest of the board:
                
                

                #this algorithm works fine for the last row i.e. from (100 <- 91)
                if player1X in range(420,631):
                    player1X-= 70*dice
                if player1X in range(0,351):
                    location = player1X/70
                    if dice > location:
                        player1X = location*70
                    elif dice<= location:
                        player1X-= 70*dice
                if player1X == 0:
                    print("YOU'VE WON!")
                print(dice)
                state ='Not_ready'
        screen.blit(board,(0,0))
        screen.blit(player1,(int(player1X),int(player1Y)))
    pygame.display.update()



























