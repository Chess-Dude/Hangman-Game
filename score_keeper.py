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

   
    def giving_score(self):
        """
        To give the score to the scoreboard
        """
        pass

   
    def update_current_score(self):
        """
        Evaluate current score
        """
        pass

   
    def re_evaluate_all_scores(self):
        """
        re-evaluates all scores
        """
        pass