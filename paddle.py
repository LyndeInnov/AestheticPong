import pygame 

BACKGROUND = (38,20,81)
Y_SIZE = 720

p_height = 100

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        #Colour the paddle, set its size
        self.image = pygame.Surface([width, height])
        self.image.fill(BACKGROUND)
        self.image.set_colorkey(BACKGROUND)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        p_height = height

        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #check for off screen event
        if self.rect.y < 0: 
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        #check for lower bound of screen
        if self.rect.y > Y_SIZE - p_height:
            self.rect.y = Y_SIZE - p_height









    