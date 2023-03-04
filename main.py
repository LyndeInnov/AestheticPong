import pygame as pg
from paddle import Paddle
from ball import Ball

pg.init()


#Define game colours 
BACKGROUND = (38,20,71)
PLAYERS = (255, 56, 100)
SCORE = (243,146,107)
BALL = (0,255,197)

#Define window size
X_SIZE = 1280
Y_SIZE = 720

#Open a new window
size = (X_SIZE, Y_SIZE)
screen = pg.display.set_mode(size)
pg.display.set_caption("Pong")

paddleA = Paddle(PLAYERS, 30, 100)
paddleA.rect.x = 80
paddleA.rect.y = 500

paddleB = Paddle(PLAYERS, 30, 100)
paddleB.rect.x = 1200
paddleB.rect.y = 500

ball = Ball(BALL, 10, 10)
ball.rect.x = X_SIZE/2
ball.rect.y = Y_SIZE/2


all_sprites_list = pg.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


#Loop will operate until use clicks close button 
carryOn = True 

#Clock used to control updating of screen 
clock = pg.time.Clock()

scoreA = 0
scoreB = 0

#Main loop

while carryOn: 
    for event in pg.event.get(): #User input
        if event.type==pg.QUIT:
            carryOn = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddleA.moveUp(5)

    if keys[pg.K_s]:
        paddleA.moveDown(5)

    if keys[pg.K_UP]:
        paddleB.moveUp(5)

    if keys[pg.K_DOWN]:
        paddleB.moveDown(5)



    all_sprites_list.update()

    if ball.rect.x>=X_SIZE-10:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>Y_SIZE-10:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    if pg.sprite.collide_mask(ball, paddleA) or pg.sprite.collide_mask(ball, paddleB):
      ball.bounce()

    screen.fill(BACKGROUND)
    pg.draw.line(screen, SCORE, [X_SIZE/2, 0], [X_SIZE/2,Y_SIZE], 8)
    
    all_sprites_list.draw(screen)

    font = pg.font.Font(None, 74)
    text = font.render(str(scoreA), 1, SCORE)
    screen.blit(text, (X_SIZE/4,10))
    text = font.render(str(scoreB), 1, SCORE)
    screen.blit(text, ((3*X_SIZE)/4,10))

    pg.display.flip()

    clock.tick(60)

pg.quit()







