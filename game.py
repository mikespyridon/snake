import pygame, sys
from src.snake import Snake
from src.food import Food
import random

# game class
class Game():
  def __init__(self):  
    self.food = Food(screen, (random.randint(75, 565), random.randint(75, 405)))
    self.food_group = pygame.sprite.GroupSingle(self.food)
    self.snake = Snake(screen, self.food, (640/2), (480/2))
    
  def run(self):

    self.snake.update()
    
    if pygame.sprite.spritecollide(self.snake, self.food_group, False):
      self.food.kill()
      self.food = Food(screen, (random.randint(75, 565), random.randint(75, 405)))
      self.food_group.add(self.food)
      self.snake.consumed = True
       
    self.food_group.draw(screen)
        
#initial setup
if __name__ == "__main__":
  pygame.init()
  
  WIDTH = 640
  HEIGHT = 480
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('Snake')
  
  FPS = 60
  clock = pygame.time.Clock()
  
  game = Game()

#game loop
while True:
  screen.fill((0,0,0))
  
  game.run()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
  pygame.display.update()
  clock.tick(FPS)
    