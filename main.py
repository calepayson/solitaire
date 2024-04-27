# Solitaire
# by: cale smith

###########
# IMPORTS #
###########

import random

#############
# CONSTANTS #
#############
CARD_VALUES = range(1, 14)
SUITS = ['H', 'C', 'D', 'S']

###########
# CLASSES #
###########

# Card: represents a playing card
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        value_conversions = {
            1:  " A",
            10: "10",
            11: " J",
            12: " Q",
            13: " K",
        }
        value_as_string = ""

        if self.value in value_conversions.keys():
            value_as_string = value_conversions[self.value]
        else:
            value_as_string = f" {self.value}"

        return f"{value_as_string}{self.suit}"

class Stack:

    def __init__(self, cards=[]):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, i=-1):
        return self.cards.pop(i)

class Deck(Stack):

    def __init__(self):
        cards = []
        for suit in SUITS:
            for value in CARD_VALUES:
                cards.append(Card(value, suit))
        super(Deck, self).__init__(cards)

class Foundation(Stack):

    def __init__(self, suit):
        cards = []
        super(Foundation, self).__init__(cards)
        self.value = 0
        self.suit = suit

    def add(self, card):
        if self.suit == card.suit and self.value == card.value - 1:
            self.cards.append(card)
            self.value += 1
        else:
            expected = Card(self.value + 1, self.suit)
            raise Exception(f"Can't add to foundation. Expected: {expected} Got: {card}")

class TableuPile(Stack):

    def __init__(self, cards=[]):
        super(TableuPile, self).__init__(cards)

    def add(self, cards):


#############
# FUNCTIONS #
#############

########
# MAIN #
########
