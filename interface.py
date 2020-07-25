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



    def get_players_guess(self, choosen_word):
        """
        Get's Player's Letter guess
        """        
        
        player_guess = input("Please enter your guess")

        return player_guess

    def print_progress(self, choosen_word):
        """
        Print's the progress
        """
        temp_value = ""

        for character in choosen_word:

            if character.isalpha() or character.isdigit():
                temp_value = temp_value + "_ "

            else:
                temp_value = temp_value + character + " "
    
        print(temp_value)
    
    def get_topic_selection(self):
        """
        Identifies if the player wants to pick the topic
        """
        random = input("Would you Like The Computer To Randomize The Topic? Yes Or No ")
        random.lower()

        if random == "yes":
            return True

        if random == "no":
            return False

    def manually_selecting_topic(self, topic_list):
        """
        Asking Player Which topic they would like to choose
        """
        print("Please Choose A Topic Of your Choice:")
        selected_topic = input(topic_list)

        return selected_topic      


    def welcome_header(self):
        """
        Welcomes the Player
        """
        print("Welcome to the Hangman game!")



