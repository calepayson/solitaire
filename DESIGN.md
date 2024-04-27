# Solitaire
By: Cale Smith

## Problem Statement

I need projects to get an interview but I haven't completed many projects

I don't understand the alure of object oriented programming

**Solution** - Code solitaire with object oriented principles

## Architectural Design

**Classes**
- **Card** - Represents a single playing card
- **Stack** - Represents an array of cards
- **Deck** - Represents a full deck
- **Foundation** - Represents a foundation pile and its rules
- **Stock** - Represents the stock pile and its rules
- **TableuPile** - Represents the TableuPile and its rules

**Logic**
1. A Deck will be initialized and shuffled
2. The Deck will be dealt onto the Tableu
3. The remaining deck will become the stock
4. While the game has not been won or forfeit:
    1. Display the board
    2. While user input is invalid:
        1. Take user input
        2. Validate user input (valid move or forfeit)
    3. Perform move logic
    4. Check for win
5. If user forfeit:
    1. Better luck next time
6. If user win:
    1. Congrats!

## Detailed Design

Card:
- Data
    - value -> int
    - suit  -> Char
- Methods
    - __init__  -> Card
    - __str__   -> String   (" VS")
Stack:
- Data
    - cards -> [Card]
- Methods
    - __init__  -> Stack
    - shuffle   -> Void     (shuffles cards)
    - draw      -> Card     (cards.pop())
Deck:
- Data
    - cards -> [Card]
- Methods
    - __init__  -> Stack    (full 52 card deck)
Foundation:
- Data
    - cards -> [Card]
- Methods
    - __init__  -> Stack
    - add       -> Void     (Checks if card can be added)
Stock:
- Data:
    - cards -> [Card]
    - mark  -> int
- Methods:
    - __init__  -> Stack
    - add       -> Void     (Checks if card can be added)
TableuPile:
- Data
    - cards -> [Card]
- Methods
    - __init__  -> Stack
    - add       -> Void     (Checks if card can be added)
    - move      -> Stack    (returns cards set cards to [])

## Construction Documentation

## Optimization
