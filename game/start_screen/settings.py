from ..global_settings import GlobalSettings

class Settings:
    """A class to store all settings for the start screen."""
    def __init__(self):
        """Initialize screen settings."""
        #Global settings.
        self.gs = GlobalSettings()
        self.screen_width = self.gs.screen_width
        self.screen_height = self.gs.screen_height
        self.bg_color = self.gs.bg_color

        #Title settings.
        self.space_size = int(self.screen_width / 7)
        self.invaders_size = int(self.screen_width / 7)
        self.space_color = (255,255,255)
        self.invaders_color = (25,206,31)

        #Button settings.
        self.button_size = int(self.screen_width / 10)
        self.button_text_color = (127,255,0)
        self.button_fill_color = (139,0,0)
        self.button_fill_color_secondary = (255,69,0)
        self.button_y = int(self.screen_height - (self.screen_height * 0.4))
