import pygame

class Snake():
  def __init__(self, screen, food, x, y):
    self.image = pygame.Surface((25,25))
    self.color = self.image.fill('green')
    self.rect = self.image.get_rect(center=(x,y))
    
    
    self.speed = 3
    self.move = [0,0]
    
    self.direction = {
      'left': False,
      'right': False,
      'up': False,
      'down': False,
      }
    
    self.food = food
    self.screen = screen
    
    self.body = [self.rect]
    self.consumed = False
    
  def get_inputs(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
      self.move[1] = -1
      self.move[0] = 0
      self.direction['up'] = True
      self.direction['down'] = False
    elif keys[pygame.K_DOWN]:
      self.move[1] = 1
      self.move[0] = 0
      self.direction['down'] = True
      self.direction['up'] = False
    elif keys[pygame.K_LEFT]:
      self.move[0] = -1
      self.move[1] = 0
      self.direction['left'] = True
      self.direction['right'] = False
    elif keys[pygame.K_RIGHT]:
      self.move[0] = 1
      self.move[1] = 0
      self.direction['right'] = True
      self.direction['left'] = False
  
    self.rect.x += self.move[0] * self.speed
    self.rect.y += self.move[1] * self.speed
  
  def collision(self):
    if self.consumed:
      if self.direction['up']:
        self.rect = pygame.Rect((self.rect.centerx - 20), (self.rect.centery - 25), 20, 20)
        self.body.append(self.rect)
      elif self.direction['down']:
        self.rect = pygame.Rect((self.rect.centerx - 20), (self.rect.centery - 25), 20, 20)
        self.body.append(self.rect)
      elif self.direction['left']:
        self.rect = pygame.Rect((self.rect.centerx - 20), (self.rect.centery - 25), 20, 20)
        self.body.append(self.rect)
      elif self.direction['right']:
        self.rect = pygame.Rect((self.rect.centerx - 20), (self.rect.centery - 25), 20, 20)
        self.body.append(self.rect)
      
      self.consumed = False
    
  def render(self):
    for chunk in self.body:
      self.screen.blit(self.image, chunk)
    
  def update(self):
    self.get_inputs()
    self.collision()
    self.render()

    
    