# Listing_18-D1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Bouncing ball program, with sprites and Clock.tick()

import pygame, sys                                                        
pygame.init()                                                            
screen = pygame.display.set_mode([640,480])                              
background = pygame.Surface(screen.get_size())                           
background.fill([255, 255, 255])                                         
clock = pygame.time.Clock()                                              
 
class Ball(pygame.sprite.Sprite):                                        
   def __init__(self, image_file, speed, location):                      
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer     
        self.image = pygame.image.load(image_file)                       
        self.rect = self.image.get_rect()                                
        self.rect.left, self.rect.top = location                         
        self.speed = speed                                               

   def move(self):                                                       
        if self.rect.left <= screen.get_rect().left or  \
                self.rect.right >= screen.get_rect().right:             
            self.speed[0] = - self.speed[0]                              
        newpos = self.rect.move(self.speed)                              
        self.rect = newpos                                               

my_ball = Ball('beach_ball.png', [10,0], [20, 20])                       

while True:                                                              
    for event in pygame.event.get():                                     
        if event.type == pygame.QUIT:                                    
            sys.exit()                                                   

    clock.tick(30)                                                       
    screen.blit(background, (0, 0))                                      
    my_ball.move()                                                       
    screen.blit(my_ball.image, my_ball.rect)                             
    pygame.display.flip()                