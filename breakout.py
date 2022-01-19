import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


# Constants that will be used in the program
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
BRICK_SEP = 4  # The space between each brick
BRICK_Y_OFFSET = 70
BRICK_WIDTH = int((APPLICATION_WIDTH - (BRICKS_PER_ROW * BRICK_SEP)) / BRICKS_PER_ROW)
BRICK_HEIGHT = 8
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
RADIUS_OF_BALL = 10
NUM_TURNS = 3

# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((255, 255, 255))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)
Paddle = pygame.sprite.Group()

p = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, BLACK)
Paddle.add(p)
p.rect.x = (APPLICATION_WIDTH/2 - PADDLE_WIDTH/2)
p.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET*4
mainsurface.blit(p.image, p.rect)

#white_p = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
#white_p.rect.x = p.rect.x
#white_p.rect.y = p.rect.y


Bricks = pygame.sprite.Group()

def row(color, row_num):
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET + ( row_num * 12)
    for x in range(BRICKS_PER_ROW):
        b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
        Bricks.add(b)
        b.rect.x = x_pos
        b.rect.y = y_pos
        mainsurface.blit(b.image, b.rect)
        x_pos += (BRICK_SEP + BRICK_WIDTH)

def two_rows(color, count):
    row(color, count + 1)
    row(color, count + 2)

def ten_rows():
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    for x in range (5):
        count = x * 2
        two_rows(colors[x], count)

ten_rows()

bal = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, 10)
bal.rect.x = (APPLICATION_WIDTH-10)/2
bal.rect.y = APPLICATION_HEIGHT/2
mainsurface.blit(bal.image, bal.rect)

#w_bal = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT, 10)
#w_bal.rect.x = w_bal.rect.x
#bal.rect.y = w_bal.rect.y
#mainsurface.blit(w_bal.image, w_bal.rect)



while True:
    mainsurface.fill(WHITE)
    mainsurface.blit(p.image, p.rect)

    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            #mainsurface.blit(white_p.image, white_p.rect)
            p.move(pygame.mouse.get_pos())
            mainsurface.blit(p.image, p.rect)
            #white_p.move(pygame.mouse.get_pos())
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if bal.rect.y > APPLICATION_HEIGHT-10:
        print("lose")  # lose screen
    if len(Bricks) <= 0:
        print("win")  # win screen

    #mainsurface.blit(w_bal.image, w_bal.rect)
    bal.move()
    bal.collide_brick(Bricks)
    bal.collide_paddle(Paddle)
    mainsurface.blit(bal.image, bal.rect)
    #w_bal.rect.x = bal.rect.x
    #w_bal.rect.y = bal.rect.y
    Bricks.draw(mainsurface)

    pygame.display.update()


