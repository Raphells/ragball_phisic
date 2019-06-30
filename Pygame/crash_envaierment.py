import pygame



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

running = 1
ball_size = 25
fps = 60
#---------------------
ball_objects = []
#-------------------------

screen.fill(white)


 
start_poz = 0,0



class BALL() :
    def __init__(self):
            self.color = (0,0,255)
            self.x = 0   # left right
            self.y = 0   # up down
            self.speed = 0      # obj_speed
            self.angle = 0      # obj_angle



def draw():
    for ball in ball_objects:
        pygame.draw.circle(screen,ball.color,(ball.x,ball.y),ball_size)



    


while running :
     ball=BALL()
     
     event = pygame.event.poll()

     if event.type == pygame.QUIT:
         running = 0
     
     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
         start_poz = event.pos
         ball.x ,ball.y = start_poz  
         ball_objects.append(ball)
         
     
         
     draw()
     clock.tick(fps)
     pygame.display.flip()