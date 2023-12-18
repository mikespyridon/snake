import pygame
import random
import time


class Food(pygame.sprite.Sprite):
  def __init__(self, screen, pos):
    super().__init__()
    self.screen = screen
    self.image = pygame.Surface((25,25))
    self.image.fill('orange')
    self.rect = self.image.get_rect(center=pos)

    
      
 

      
     
  
  
        
    
    
  