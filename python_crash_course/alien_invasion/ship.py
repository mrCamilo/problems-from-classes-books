import pygame

class Ship:
    """Manages ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store ship horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update position from moevement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
