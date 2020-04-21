import random

def newCard():
    #Randomly selects a string to return from A - K
    card = random.randint(1,13)
    if card == 1:
        return 'A'
    elif card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    else:
        return str(card)

def toInt(card):
    #takes in a card value, didn't use any constructors
    tens = ['J', 'Q', 'K']
    if card == "A":
        print('Do you want Ace to be 1 or 11?')
        x = input()
        if x == "1":
            return 1
        elif x == "11":
            return 11
        elif x != 1 and x != 11:
            print('Please choose 1 or 11! Run toInt again! ')
            return
    elif card in tens:
        return 10
    elif card in ['2', '3', '4', '5', '6', '7', '8', '10']:
        return int(card)
    else:
        print("Not a valid card! Run toInt again!")
        return