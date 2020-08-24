import sys
from time import sleep

from game.global_settings import GlobalSettings
from game.start import StartScreen
from game.main import MainScreen

if __name__ == '__main__':
    gs = GlobalSettings()
    start = StartScreen(gs)
    main = MainScreen(gs) #Main screen where the user plays the game
    while True:
        if gs.screen_name == "main":
            main.run_game()
        elif gs.screen_name == "start":
            start.start_game()
        elif gs.screen_name == "game_over":
            sys.exit()

        #Pause the game before changing screen.
        sleep(0.3)
