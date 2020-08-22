from screeninfo import get_monitors

class GlobalSettings:
    """A class to store all settings for the game."""
    def __init__(self):
        """Initialize game settings."""
        #Monitor size used as reference for screen size.
        self.monitor_width, self.monitor_height = self._get_monitor_size()

        #Screen settings.
        self.screen_name = "start"
        self.screen_width = int(self.monitor_width / 1.2)
        self.screen_height = int(self.monitor_height / 1.2)
        self.bg_color = (15, 15, 15)


    def _get_monitor_size(self):
        """Get the size of the bigger monitor."""
        max_width = 0
        max_height = 0
        for m in get_monitors():
            if m.width > max_width:
                max_width = m.width
            if m.height > max_height:
                max_height = m.height

        return (max_width, max_height)
