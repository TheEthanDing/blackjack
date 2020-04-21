import random
from cards import * 
from support import *

""" 
printOneCard(a):
prints out one card, with value a

printTwoCards(a, b):
prints out two cards, with values a then b

def toInt(card):
return an int corresponding to card string value

def newCard():
return a random string from A - K
"""

#This is the introduction 
print('Welcome to Blackjack')
print('These are your cards')
yourCard1 = newCard()
yourCard2 = newCard()
printOneCard(yourCard1)
newCards = []
printTwoCards(yourCard1, yourCard2)
yourValue = toInt(yourCard1) + toInt(yourCard2)

print('These are the dealer\'s cards')
dealerCard1 = newCard()
dealerCard2 = newCard()
dealerCards = []
printTwoCards(dealerCard1, dealerCard2)
dealerValue = toInt(dealerCard1) + toInt(dealerCard2)

"""
loop = True
while loop:
    print('What do you do? (Type H for hit, S for stay)')
    command = input()
    if command == 'H' or command == 'h':
        print('Hit!')
        nextCard =
    elif command == 'S' or command = 's':
        print('Stay!')
        loop = False
    else:
        print('Fuck you')"""
#print('your first card is a', x)
