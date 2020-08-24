import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

       # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()#_alpha()
        # threshold = 128
        # for x in range(self.image.get_width()):
        #     for i in range (self.image.get_height()):
        #         color = self.image.get_at(x,y)
        #         if color.r > threshold and color.g > threshold and color.b > threshold:
        #             self.image.set_at((x,y),(0,0,0,0)
        self.image.set_colorkey((230, 230, 230))
        
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self): 
        #Update the ship's position
        #Update the ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
                #    """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)



class Character:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/darth-vader.bmp')
        self.image = pygame.transform.scale(self.image,(80,50))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)         

        




