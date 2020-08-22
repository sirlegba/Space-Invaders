import sys

import pygame

from game.global_settings import GlobalSettings
from .start_screen.settings import Settings
from .start_screen.title import Title
from .start_screen.play_button import PlayButton

class StartScreen:
    """Overall class to manage game assets and behavior of the main game screen."""

    def __init__(self, global_settings):
        """Initialize the start menu game and the game resources."""
        pygame.init()

        self.gs = global_settings
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.gs.screen_width, self.gs.screen_height))
        pygame.display.set_caption("Space Invaders")

        self._create_title()
        self._create_play_button()

    def _create_title(self):
        font = pygame.font.SysFont(None, self.settings.space_size)
        width, height = font.size("SPACE")
        self.space = Title(self, "SPACE", 0, font, self.settings.space_color)
        self.invaders = Title(self, "INVADERS", height, font, self.settings.invaders_color)

    def _create_play_button(self):
        font = pygame.font.SysFont(None, self.settings.button_size)
        self.button = PlayButton(self, "PLAY", self.settings.button_y, font, self.settings.button_text_color, self.settings.button_fill_color)

    def start_game(self):
        """Start the main loop for the game."""

        # Show the mouse cursor.
        pygame.mouse.set_visible(True)

        while self.gs.screen_name == "start":
            self._check_events()
            self._change_button_colors()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.gs.screen_name = "main"
            elif event.type == pygame.QUIT:
                sys.exit()

    def _change_button_colors(self):
        """Change the colors of the button when the mouse is over."""
        if self.button.rect.collidepoint(pygame.mouse.get_pos()):
            self.button.fill_color = self.settings.button_fill_color_secondary
        else:
            self.button.fill_color = self.settings.button_fill_color

    def _check_play_button(self):
        """Start a new game when the player clicks Play."""
        if self.button.rect.collidepoint(pygame.mouse.get_pos()):
            self.gs.screen_name = "main"

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Print Background.
        self.screen.fill(self.gs.bg_color)

        self.space.draw_title()
        self.invaders.draw_title()
        self.button.draw_button()

        #Set the newest screen as the visible one.
        pygame.display.flip()
