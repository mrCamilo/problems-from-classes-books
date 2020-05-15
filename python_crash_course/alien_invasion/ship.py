import pygame

class Ship:
    """Manages ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
