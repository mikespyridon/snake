import pygame, sys

# game class
class Game():
  def __init__(self):
    pass
    
  def run(self):
    pass
    
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
    