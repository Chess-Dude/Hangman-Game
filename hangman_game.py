"""
This is a digitalized version of the classic hangman game
The rules are listed below:
*rick roll music starts*
"""

from interface import Interface
from score_keeper import ScoreKeeper
import word_selector
from scoreboard import Scoreboard

def run_game():
    """
    runs the game
    """
    
    interface_obj = Interface()
    player_name = interface_obj.get_player_name()
    interface_obj.welcome_header()
    random = interface_obj.get_topic_selection()
    wordselector_obj = word_selector.WordSelector()
    if random:
        selected_topic = wordselector_obj.get_random_topic()

    else: 
        selected_topic = interface_obj.manually_selecting_topic(wordselector_obj.topic_list)
    choosen_word = wordselector_obj.select_word(selected_topic)
    interface_obj.print_progress(choosen_word)
    player_guess = interface_obj.get_players_guess(choosen_word)
    scorekeeper_obj = ScoreKeeper(player_name, 0, 0)
    scorekeeper_obj.update_current_score(choosen_word, player_guess)
    

if __name__ == "__main__":
    run_game()