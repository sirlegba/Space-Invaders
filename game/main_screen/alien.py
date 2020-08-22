import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet and control the whole fleet."""

    def __init__(self, game, type, points):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.type = type
        self.points = points
        self.screen = game.screen
        self.settings = game.settings

        #Load the 2 alien images and resize them.
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load(f'resources/images/{self.type}A.bmp'), (self.settings.alien_width, self.settings.alien_height)))
        self.images.append(pygame.transform.scale(pygame.image.load(f'resources/images/{self.type}B.bmp'), (self.settings.alien_width, self.settings.alien_height)))
        self.images.append(pygame.transform.scale(pygame.image.load(f'resources/images/{self.type}C.bmp'), (self.settings.alien_width, self.settings.alien_height)))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.index = 0

        #Variable to know when to remove the alien image.
        self.time_die = 0

        #Exact alien position.
        self.x = 0

    def update(self):
        """Move the alien to left or right and change the alien image."""
        self.x += (self.settings.alien_movement * self.settings.fleet_direction)
        self.rect.x = self.x

        screen_rect = self.screen.get_rect()

        self.update_image()

    def update_image(self):
        if self.time_die > 0:
            self.index = 2
        else:
            self.index +=1
            if self.index >= 2:
                self.index = 0
        self.image = self.images[self.index]

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def destroy(self):
        self.time_die = pygame.time.get_ticks() + 30
        self.image = self.images[2]

    @staticmethod
    def create_fleet(self, settings):
        fleet = pygame.sprite.Group()

        for i in range(5):
            for x in range(12):
                if i == 0:
                    type = "squid"
                    points = 40
                elif i < 3:
                    type = "crank"
                    points =20
                else:
                    type = "octopus"
                    points = 10

                alien = Alien(self, type, points)
                alien.rect.x = self.settings.fleet_position + (settings.fleet_left_space + settings.alien_width) * x
                alien.rect.y = settings.alien_height + (settings.fleet_top_space + settings.alien_height) * i

                alien.x = float(alien.rect.x)
                fleet.add(alien)

        return fleet
