import pygame
import random
import math 


running = 1
width = 640
hight = 480
screen = pygame.display.set_mode((width, hight))
clock = pygame.time.Clock()

# --------------------- predefine colors
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
gren = (0,255,0)
#----------------------------------------

#--------------------- predefine constans
fps = 60
elasticity = 0.70
gravity = 9.81/fps*2   #9,81

size = 20





class Ball():
    def __init__(self):
        self.x = 100
        self.y = 50
        self.force_x = 0
        self.force_y = 0
        self.speed = 0
        self.angle = 1      
        


def draw():
    for ball in balls_obj:
        pygame.draw.circle(screen,red,(ball.x,ball.y),size)

def move ():  
    
    
    for ball in balls_obj:

       
        
           ball.speed += ball.angle * gravity
           ball.y += int(ball.angle *ball.speed)
           print(ball.y,ball.speed,ball.angle)


def bounce():
    for ball in balls_obj:

        if ball.y > hight-22 and ball.angle == 1:
            ball.angle = -1
            ball.speed*=elasticity
            
        if ball.speed < 0 :
            ball.angle = 1
        if ball.y == hight-21 and ball.speed > -0.2 and ball.speed < 0.2 :
           balls_obj.remove(ball)




balls_obj = []


while running:
    ball = Ball()
    screen.fill(white)
    
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
         running = 0
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        ball.x,ball.y = event.pos
        balls_obj.append(ball)
        
        

    screen.fill((255, 255, 255))
    bounce()
    move()
    draw()
    
    clock.tick(fps)
    pygame.display.flip()    





