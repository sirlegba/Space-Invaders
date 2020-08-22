class GameStats:

    def __init__(self, settings):
        """Track statistics for Alien Invasion."""
        self.settings = settings

        self.high_score = 0
        self.level = 1
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.alien_speed = self.settings.alien_speed
        self.alien_level_speed = self.settings.alien_speed

    def increase_level(self):
        """Increase the difficulty of the game by updating aliens' speed."""
        self.level += 1

        if self.alien_speed > 20:
            self.alien_speed -= 20
        elif speed > 1:
            self.alien_speed -= 1
        elif speed > 0.01:
            self.alien_speed -= 0.01

        self.alien_level_speed = self.alien_speed

    def alien_hit(self, points):
        """Increase the score and difficulty of the level"""
        if self.alien_level_speed > 15:
            self.alien_level_speed -= 15
        self.score += points
