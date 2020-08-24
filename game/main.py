import sys
from time import sleep

import pygame

from .main_screen.settings import Settings
from .main_screen.ship import Ship
from .main_screen.alien import Alien
from .main_screen.bullet import Bullet
from .main_screen.scoreboard import Scoreboard
from .main_screen.game_stats import GameStats

class MainScreen:
    """Manage game assets and behavior of the main game screen."""

    def __init__(self, global_settings):
        """Initialize the game and the game resources."""
        pygame.init()

        self.gs = global_settings
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        self.ship = Ship(self)
        self.fleet = Alien.create_fleet(self, self.settings)
        self.bullets = pygame.sprite.Group()
        self.stats = GameStats(self.settings)
        self.sb = Scoreboard(self)

        self.fleet_downed = False
        self.alien_move_next = pygame.time.get_ticks() + self.stats.alien_speed

    def run_game(self):
        """Start the main loop for the game."""

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        while self.gs.screen_name == "main":
            self.current_time = pygame.time.get_ticks()
            self._check_events()
            self._remove_shooted_aliens()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.m_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.m_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.m_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.m_left = False

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.fleet, True, False)
        if collisions:
            for collision in collisions.values():
                for alien in collision:
                    alien.destroy()
                    self.stats.alien_hit(alien.points)
            self.sb.prep_score()

        if not self.fleet:
            #Remove all bullets, create a new fleet and increase level.
            self.bullets.empty()
            self.fleet = Alien.create_fleet(self, self.settings)
            self.stats.increase_level()
            self.sb.prep_level()

    def _remove_shooted_aliens(self):
        for alien in self.fleet:
            if alien.time_die > 0 and alien.time_die <= self.current_time:
                self.fleet.remove(alien)

    def _update_alien(self):
        if self.alien_move_next <= self.current_time:
            if not self._check_fleet_edges():
                self.fleet.update()
                self.fleet_downed = False
            self.alien_move_next = self.current_time + self.stats.alien_level_speed

        if pygame.sprite.spritecollideany(self.ship, self.fleet):
            self._ship_hit()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                if not self.fleet_downed:
                    self._change_fleet_direction()
                    self.fleet_downed = True
                    return True
        return False

    def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            #Rest one life and update scoreboard.
            self.stats.ships_left -=1
            self.sb.prep_ships()

            #Delete aliens and bullets left.
            self.fleet.empty()
            self.bullets.empty()

            #Create a new fleet and ship.
            self.fleet = Alien.create_fleet(self, self.settings)
            self.ship.center_ship()

            #Reset alien's speed
            self.stats.alien_level_speed = self.stats.alien_speed

            #Pause the game.
            sleep(0.5)
        else:
            self.gs.screen_name = "game_over"

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.fleet.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            alien.update_image()
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Print Background.
        self.screen.fill(self.settings.bg_color)

        #Draw sprites.
        self.ship.draw()
        self.fleet.draw(self.screen)
        self.sb.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw()

        self.clock.tick(30)

        #Set the newest screen as the visible one.
        pygame.display.flip()
