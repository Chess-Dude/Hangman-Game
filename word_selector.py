"""
Selects the topic then the word
"""

import random

class WordSelector:
    """
    Selects the topic then the word
    """
    
    def __init__(self):
        self.topic_list = ["Kitchenware", "Sports", "Furniture", "Food"]
        self.word_list = None
        self.selected_topic = None
        self.selected_word = None



    def get_random_topic(self):
        """
        If random is True then computer picks a topic
        If random is fale then player picks a topic
        """
        choosen_topic = random.choice(self.topic_list)

        return choosen_topic



    def select_word(self, choosen_topic):
        """
        Selects the choosen word by identifying the selected topic
        """
        
        choosen_word = ""
        # If statements, Checking for chosen topic
            # Inside if statments list of possible words/phrases, for one to be randomized
        if choosen_topic == "Kitchenware":
            print("The topic is kitchenware")
            phrases = ["fork", "plate", "cup", "spoon", "pot", "bowl", "pan", "dish", "knife"]
            choosen_word = random.choice(phrases)

        elif choosen_topic == "Sports":
            print("The topic is Sports")
            phrases = ["ball", "net", "goal", "score", "racket", "active", "kick"]
            choosen_word = random.choice(phrases)

        elif choosen_topic == "Furniture":
            print("The topic is Furniture")
            phrases = ["couch", "chair", "television", "table", "desk", "bookshelf"]
            choosen_word = random.choice(phrases)

        elif choosen_topic == "Food":
            print("The topic is Food")
            phrases = ["banana", "potato", "toast", "rice", "delicious", "carrot", "cake", "tiramisu", "yummy"]
            choosen_word = random.choice(phrases)
    
        return choosen_word