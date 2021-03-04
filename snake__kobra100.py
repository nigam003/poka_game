import pygame
import random
import  math

pygame.init()
#display
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('snake__kobra100')
icon=pygame.image.load('anaconda.png')
pygame.display.set_icon(icon)
background_pic=pygame.image.load('beautiful-space-background.1.png')
#snake head
snake=pygame.image.load('snake_head.png')
snake_haed_x=400
snake_haed_y=300
snake_haed_x_change=0
snake_haed_y_change=0
# body
body=pygame.image.load('body.png')
body_x=random.randint(64,736)
body_y=random.randint(64,536)
body_x_change=0
body_y_change=0


def body1(x, y):
    screen.blit(body, (x, y))

def snake_head(x,y):
    screen.blit(snake,(x,y))


#eat
def iseat(snake_haed_x,snake_haed_y,food_x,food_y):
    d= math.sqrt(math.pow((snake_haed_x-food_x),2)+math.pow((snake_haed_y-food_y),2))
    if d<27:
        return True
    else:
        return False
#game over
def isover(snake_haed_x,snake_haed_y,body_x,body_y):
    a=math.sqrt(math.pow((snake_haed_x-body_x),2)+math.pow((snake_haed_y-body_y),2))
    if a<45:
        return True
    else:
        return False
    # food
food = pygame.image.load('food.png')
food_x = random.randint(64, 736)
food_y = random.randint(64, 536)
food_x_change = 0
food_y_change = 0
score = 0
def food_(x,y):
    screen.blit(food,(x,y))


run =True
while run:
    screen.fill((0,0,255))
    screen.blit(background_pic,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_haed_x_change = -1
            if event.key == pygame.K_RIGHT:
                snake_haed_x_change = 1


        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_UP:
                snake_haed_y_change = -1

            if event.key == pygame.K_DOWN:
                snake_haed_y_change = 1



    #movement of snake's head
    snake_haed_x += snake_haed_x_change
    snake_haed_y += snake_haed_y_change
    if snake_haed_x >800:
        snake_haed_x =0
    elif snake_haed_x <0:
        snake_haed_x =800
    if snake_haed_y > 600:
        snake_haed_y = 0
    elif snake_haed_y < 0:
        snake_haed_y = 600

   #food change

    eat = iseat(snake_haed_x, snake_haed_y, food_x, food_y)
    if eat:
       food_x_change1 = food_x_change+random.randint(64,736)
       food_y_change1 = food_y_change +random.randint(64,536)
       food_x=food_x_change1
       food_y=food_y_change1
       score=score+1
       print(score)
        # game over logic
    over =isover(snake_haed_x,snake_haed_y,body_x,body_y)
    if over:
        snake_haed_x=1000
        snake_haed_y=1000
        print("game over")
        score=0

   #body movement
    body_x +=2
    body_y +=2
    body_x_change1 = body_x_change + random.random() * 0.1
    body_x_change2 = body_x_change + random.random() * (-0.1)
    body_y_change1 = body_y_change + random.random() * 0.1
    body_y_change2 = body_y_change + random.random() * (-0.1)

    if body_x< 0:
        body_x =body_x_change1

    elif body_x >800:


        body_x =body_x_change2

    if body_y <0:


        body_y += body_y_change1
    elif body_y >600:


        body_y = body_y_change2



    snake_head(snake_haed_x,snake_haed_y)
    food_(food_x,food_y)
    body1(body_x,body_y)
    pygame.display.update()