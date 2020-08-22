import pygame.font

class Title:
    """Title of the game."""

    def __init__(self, game, msg, y, font, color):
        """Initialize the title, set a text and center it."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.msg = msg
        self.font = font
        self.color = color
        self.width, self.height = self.font.size(msg)

        #Create a rect for the object and center it at the top.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = y

        #Prepare title texts.
        self._prep_text()

    def _prep_text(self):
        """Transform text into an image and center it."""
        self.msg_image = self.font.render(self.msg, True, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_title(self):
        """Dibuja un boton en blanco y despues le dibuja un texto."""
        #self.screen.fill((30,30,50), self.rect) #Dibujar la posicion rectangular del boton.
        self.screen.blit(self.msg_image, self.msg_image_rect) #Dibujar el texto dentro del boton.
