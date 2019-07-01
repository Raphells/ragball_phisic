import pygame
import random
import math

#------------ Color--------------
red = (255,0,0)
green = (0,0,255)
blue = (0,255,0)
orange = (236,77,0)
pink = (255,0,128)
white = (255, 255, 255)
#--------------------------------
#-----------Global variables-------
width, height = (800, 600)

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 60
running = 1
ball_size = 10
elasticity = 0.9
gravity = 9.81/fps*2   #9,81
start_poz = 0,0

#---------------------
ball_objects = []
#-------------------------




 
screen.fill(white)









class BALL() :
    def __init__(self):
            self.color = (0,0,255)
            self.x = 0  # left right
            self.y = 0   # up down
            self.speed = 0      # obj_speed 
            self.angle = 0      # obj_angle
            
    def draw(self):
        
            pygame.draw.circle(screen,self.color,(self.x,self.y),ball_size)

    def move(self):

        x = math.sin(self.angle)*self.speed
        y = math.cos(self.angle)*self.speed+math.cos(math.pi)*gravity
        
        
        self.angle = 0.5 *  math.pi - math.atan2(y,x)

        self.speed = math.hypot(x,y)
        

        self.x += int(math.sin(self.angle)*self.speed)
        self.y -= int(math.cos(self.angle)*self.speed)
        

    def bouncing(self):

            if self.x > width - ball_size:
                self.x = 2*(width - ball_size) - self.x
                self.angle = -self.angle
                self.speed *=elasticity
                
            if self.x < ball_size:
                self.x = 2*ball_size - self.x
                self.angle = -self.angle
                self.speed *=elasticity
                
            if self.y > height-ball_size :
                self.y = 2*(height - ball_size) - self.y
                self.angle = math.pi - self.angle 
                self.speed*=elasticity
                
            if self.y < ball_size :
                self.y = 2*ball_size - self.y
                self.angle = math.pi - self.angle 
                self.speed*=elasticity
                

    


while running :
     ball=BALL()
     
     event = pygame.event.poll()
     screen.fill((255, 255, 255))
     if event.type == pygame.QUIT:
         running = 0
     
     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
         ball.x , ball.y = event.pos
         ball.speed = 20 
         ball.angle = math.radians(-15)
         ball_objects.append(ball)
         
         
         
     
     for ball in ball_objects   : 
        ball.draw()
        ball.move()
        ball.bouncing()
        
     clock.tick(fps)
     pygame.display.flip()