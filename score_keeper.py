"""
Keeps the score of the player
"""

class ScoreKeeper:
    """ 
    keeps the score of the player
    """
   
   
    def __init__(self, player_name, highest_score, lowest_score):
        self.player_name = ""
        self.highest_score = highest_score
        self.lowest_score = lowest_score
        self.current_score = 0
        self.correct_guesses = []
        self.wrong_guesses = []
        self.total_lives = 6
   
    def giving_score(self):
        """
        To give the score to the scoreboard
        """
        pass

   
    def update_current_score(self, choosen_word, player_guess):
        """
        Evaluate current score
        """
        MAX_SCORE = len(choosen_word)
                
        # Check if player's guess is in the choosen word
        if player_guess in choosen_word:
            print("Good Job Your Guess Is In The Word!")
            # Check if the player's guess is already a letter guesses
            if player_guess not in self.correct_guesses:
                # If false appened the player's guess to the correct guesses list
                self.correct_guesses.append(player_guess)
                # Counting How many times each letter occurs in choosen word
                occurances = choosen_word.count(player_guess)
                self.current_score = self.current_score + occurances
                if self.current_score == MAX_SCORE:
                    print("Congrats! You have won the game!")


            else:
                print("You have already Guessed this letter, please guess again")    

        else:
            print("Sorry That letter is not in the word. Please try again")
            if player_guess not in self.wrong_guesses:
                self.wrong_guesses.append(player_guess)
                self.total_lives = self.total_lives - 1
                if self.total_lives == 0:
                    "You have hanged the man."

            else: 
                print("You've already guessed this letter AND ITS WRONG") 




   
    def re_evaluate_all_scores(self):
        """
        re-evaluates all scores
        """
        pass