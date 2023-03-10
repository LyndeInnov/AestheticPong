import pygame
from random import randint
BG = (38,20,71)

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height):
        super().__init__()
        # Pass in the colour of the ball, and dimensions 
        self.image = pygame.Surface([width, height])
        self.image.fill(BG)
        self.image.set_colorkey(BG)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)






        
