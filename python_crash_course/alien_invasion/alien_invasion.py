# Pygame window, responding to user input

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        def run_game(self):
            """Start the main loop for the game"""
            while True:
                self._check_events()
                self._update_screen()

        def _check_events(self):
            """Respond to keypresses, mouse events.""" 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        def _update_screen(self):
            """Update images on screen, flip to new screen"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

#class Ship:                                                    
 #   """A class to manage the ship."""
  #  def __init__(self, ai_game):
   #     self.screen = ai_game.screen
    #    self.screen_rect = ai_game.screen.get_rect()
 
        #Load ship image, get its rect.
     #   self.image = pygame.image.load('images/ship.bmp')
      #  self.rect = self.image.get_rect()
 
     #Start each new ship at the bottom center of the screen.
    #self.rect.midbottom = self.screen_rect.midbottom
 
#    def blitme(self):
 #       "Draw the ship at its current location."
  #      self.screen.blit(self.image, self.rect)
