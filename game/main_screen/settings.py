from ..global_settings import GlobalSettings

class Settings:
    """A class to store all settings for the game."""
    def __init__(self):
        """Initialize game settings."""
        #Global settings
        self.gs = GlobalSettings()
        self.screen_width = self.gs.screen_width
        self.screen_height = self.gs.screen_height
        self.bg_color = self.gs.bg_color

        #Ship settings.
        self.ship_width = int(self.screen_width / 12)
        self.ship_height = int(self.screen_height / 8)
        self.ship_speed = int(self.ship_width / 10)
        self.ship_limit = 3

        #Alien settings.
        self.alien_width = int(self.screen_width / 20)
        self.alien_height = int(self.screen_height / 15)
        self.fleet_left_space = int(self.alien_width / 4)
        self.fleet_top_space = int(self.alien_height / 4)
        self.fleet_position = (self.screen_width - 12 * self.alien_width - 12 * self.fleet_left_space + self.alien_width / 2)  / 2 #Center the fleet based on the fleet size (alien + spaces) plus the spaces from both sides (half alien). Substracted to the screen width and divided by two it gives the margins of both sides.
        self.alien_movement = self._calculate_alien_movement()
        self.alien_speed = 1000
        self.fleet_drop_speed = int(self.alien_height / 4)
        self.fleet_direction = 1


        #Bullet settings.
        self.bullet_width = int(self.ship_width / 20)
        self.bullet_height = int(self.ship_height / 4)
        self.bullet_color = (242, 242, 13)
        self.bullets_allowed = 3
        self.bullet_speed = int(self.bullet_height / 1.2)

        #Scoreboard settings.
        self.sb_ship_width = int(self.screen_width / 24)
        self.sb_ship_height = int(self.screen_height / 18)
        self.sb_ship_separation = int(self.screen_height / 80)

    def _calculate_alien_movement(self):
        """Calculate the pixels that alien moves based on the common divisors between float size and screen width."""
        float_size = 12 * self.alien_width + 11 * self.fleet_left_space
        for i in range (50, 0, -1): #The maximum speed will be 50.
            if self.screen_width % i == 0 and float_size % i == 0:
                return i
