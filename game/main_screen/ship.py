import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        #Load the ship image and resize it.
        self.image = pygame.image.load('resources/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Ship's horizontal position.
        self.x = float(self.rect.x)

        #Movement flags.
        self.m_right = False
        self.m_left = False


    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.m_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.m_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
