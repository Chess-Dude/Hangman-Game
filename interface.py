"""
Get's Player's input and sends input to other classes
"""

class Interface:
    """
    Takes input from player. Processes the input, formats the output text.
    """

    
    def __init__(self):
        self.players_input = ""

    
    def get_input(self):
        """
        Get's any input needed
        """
        pass


    def get_player_name(self):
        """
        Gets player's Name
        """
        player_name = input("What's your name?")

        return player_name



    def get_players_guess(self):
        """
        Get's Player's Letter guess
        """
        pass


    def get_topic_selection(self):
        """
        Identifies if the player wants to pick the topic
        """
        pass


    def welcome_header(self):
        """
        Welcomes the Player
        """
        print("Welcome to the Hangman game!")



