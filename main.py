# Solitaire
# by: cale smith

###########
# IMPORTS #
###########

import random

#############
# CONSTANTS #
#############
MAX_VALUE = 14
CARD_VALUES = range(1, MAX_VALUE)
SUITS = ['H', 'C', 'D', 'S']
RED = 1
BLACK = 2
TABLEU_PILES = 7
EMPTY_PILES = ['   ', '   ', '   ', '   ', '   ', '   ', '   ']
VALID_MOVES = ['0', '1', '2', '3', '4', '5', '6', '7', 'h', 'c', 'd', 's', 'n', 'q', 'h']

###########
# CLASSES #
###########

# Card: represents a playing card
class Card:

    def __init__(self, value, suit):
        self.value = value
        if suit == 'H' or suit == 'D':
            self.color = RED
        elif suit == 'C' or suit == 'S':
            self.color = BLACK
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

    def draw(self, index=-1):
        return self.cards.pop(index)

class Deck(Stack):

    def __init__(self):
        cards = []
        for suit in SUITS:
            for value in CARD_VALUES:
                cards.append(Card(value, suit))
        super(Deck, self).__init__(cards)

    def popAll(self):
        cards = self.cards
        self.cards = []
        return cards

class Foundation(Stack):

    def __init__(self, suit):
        cards = []
        super(Foundation, self).__init__(cards)
        self.value = 0
        self.suit = suit

    def addCard(self, card):
        self.cards.append(card)
        self.value += 1

    def getTop(self):
        if len(self.cards) == 0:
            return f" 0{self.suit}"
        else:
            return f"{self.cards[-1]}"

    def validate(self, card):
        if self.suit == card.suit and self.value == card.value - 1:
            return True
        else:
            return False


class Stock(Stack):

    def __init__(self, cards):
        super(Stock, self).__init__(cards)
        self.mark = 2

    def showHand(self):
        window = []
        result = ""
        if self.mark == 0:
            window = [0]
        elif self.mark == 1:
            window = [0, 1]
        else:
            window = range(max(0, self.mark-2), min(self.mark+1, len(self.cards)))
        for i in window:
            result += f"{self.cards[i]}"
        return result

    def drawStockCard(self):
        self.mark -= 1
        return self.cards.pop(self.mark+1)
    
    def newHand(self):
        end = len(self.cards) - 1
        
        if self.mark == end:
            self.mark = 2
        elif self.mark + 3 > end:
            self.mark = end
        else: 
            self.mark += 3

    def getCard(self):
        return self.cards[self.mark]


class TableuPile(Stack):

    def __init__(self, cards=[]):
        super(TableuPile, self).__init__(cards)

    def addCard(self, card):
        self.cards.append(card)

    def addStack(self, cards):
        self.cards += cards

    def validate(self, card):
        if len(self.cards) == 0:
            if card.value == 13:
                return True
            else:
                return False

        value1 = self.cards[-1].value
        color1 = self.cards[-1].color

        value2 = card.value
        color2 = card.color

        if value1 == value2 + 1 and color1 != color2:
            return True
        else:
            return False

    def move(self):
        cards = self.cards
        self.cards = []
        return cards

    def getRootCard(self):
        return self.cards[0]

    def getFirstCard(self):
        if len(self.cards) > 0:
            return self.cards[-1];
        else:
            return Card(0, 'S')

    def takeCard(self):
        return self.draw()

class Move:

    def __init__(self):
        self.source = ''
        self.dest = ''
        self.command = ''
        
        while self.source not in VALID_MOVES:
            source = input("From: ")
            if source in ['q', 'n']:
                self.command = source
                return
            else:
                self.source = source

        while self.dest not in VALID_MOVES:
            source = input("To: ")
            if source in ['q', 'n']:
                self.command = source
                return
            else:
                self.dest = source




#############
# FUNCTIONS #
#############

def display_board(foundations, tableu_piles, stock):
    hearts = ""
    clubs = ""
    diamonds = ""
    spades = ""

    for i in range(0, len(foundations)):
        match (foundations[i].suit):
            case "H":
                hearts = f"{foundations[i].getTop()}"
            case "C":
                clubs = f"{foundations[i].getTop()}"
            case "D":
                diamonds = f"{foundations[i].getTop()}"
            case "S":
                spades = f"{foundations[i].getTop()}"
    
    print(f" {hearts} {clubs} {diamonds} {spades} {stock.showHand()}")

    tableu_pile_lengths = []
    for i in range(0, TABLEU_PILES):
        length = len(tableu_piles[i].cards)
        tableu_pile_lengths.append(length)

    for i in range(0, MAX_VALUE):
        line = EMPTY_PILES
        for j in range(0, TABLEU_PILES):
            if tableu_pile_lengths[j] > i:
                line[j] = str(tableu_piles[j].cards[i])
            else:
                line[j] = '   '
        print(' '.join(line))

def stock_to_foundation(stock, foundation):
    temp_card = stock.getCard()
    if foundation.validate(temp_card):
        card = stock.drawStockCard()
        foundation.addCard(card)
    else:
        print("Not a valid move")

def tableu_to_foundation(tableu, foundation):
    temp_card = tableu.getFirstCard()
    if foundation.validate(temp_card):
        card = tableu.takeCard()
        foundation.addCard(card)

def stock_to_tableu(stock, tableu):
    temp_card = stock.getCard()
    if tableu.validate(temp_card):
        card = stock.drawStockCard()
        tableu.addCard(card)

def tableu_to_tableu(tableu1, tableu2):
    temp_card = tableu1.getRootCard()
    if tableu2.validate(temp_card):
        stack = tableu1.move()
        tableu2.addStack(stack)

def get_type(move):
    match (move):
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' :
            return "tableu"
        case 'h' | 'c' | 'd' | 's':
            return "foundation"
        case '0':
            return "stock"
        case _:
            return f"Error, unrecognized move: {move}"

def get_foundation_index(c):
    match (c):
        case 'h':
            return 0
        case 'c':
            return 1
        case 'd':
            return 2
        case 's':
            return 3
        case _:
            raise Exception("Error")


########
# MAIN #
########

def main():
    deck = Deck()
    deck.shuffle()
    foundations = []
    stacks = []
    tableu_piles = []

    
    for suit in SUITS:
        foundations.append(Foundation(suit))

    for i in range(0, TABLEU_PILES):
        stack = Stack(cards=[])
        for j in range(0, i):
            stack.cards.append(deck.draw())

        stacks.append(stack)
        tableu_piles.append(TableuPile([deck.draw()]))

    stock = Stock(deck.popAll())
            
    while True:
        len_h = len(foundations[0].cards)
        len_c = len(foundations[1].cards)
        len_d = len(foundations[2].cards)
        len_s = len(foundations[3].cards)

        if len_h >= 13 and len_c >= 13 and len_d >= 13 and len_s >= 13:
            break

        # Display playing board
        display_board(foundations, tableu_piles, stock)

        # Gets player move
        move = Move()

        # Handles any commands 
        if move.command == 'q':
            print("Better luck next time!")
            return
        elif move.command == 'n':
            stock.newHand()

        # Gets the type for each source
        source_type = get_type(move.source)
        dest_type = get_type(move.dest)

        # Make a move boi
        if source_type == "stock" and dest_type == "foundation":
            i = get_foundation_index(move.dest)
            stock_to_foundation(stock, foundations[i])
        elif source_type == "tableu" and dest_type == "foundation":
            i = get_foundation_index(move.dest)
            tableu_to_foundation(tableu_piles[int(move.source)-1], foundations[i])
        elif source_type == "stock" and dest_type == "tableu":
            stock_to_tableu(stock, tableu_piles[int(move.dest)-1])
        elif source_type == "tableu" and dest_type == "tableu":
            tableu_to_tableu(tableu_piles[int(move.source)-1], tableu_piles[int(move.dest)-1])

        # draw stacks
        for i in range(0, TABLEU_PILES):
            if len(tableu_piles[i].cards) < 1:
                if len(stacks[i].cards) > 0:
                    tableu_piles[i].addCard(stacks[i].draw())

    display_board(foundations, tableu_piles, stock)
    print("WOOOOOOO!!!!! YOU DA BEST!!!! YAAAAAAA!!!!")

main()
