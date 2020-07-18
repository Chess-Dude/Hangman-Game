"""
This is a digitalized version of the classic hangman game
The rules are listed below:
*rick roll music starts*
"""

from interface import Interface
from score_keeper import ScoreKeeper
from word_selector import WordSelector
from scoreboard import Scoreboard

def run_game():
    """
    runs the game
    """
    
    interface_obj = Interface()
    interface_obj.welcome_header()
    player_name = interface_obj.get_player_name()
    print("Welcome", player_name, "To the hangman game!")

    

if __name__ == "__main__":
    run_game()