#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:10:29 2018

@author: beniamin
"""

import random 

deck = [{'Card': 'A', 'Color': 'Spades', 'Power' : 11},
        {'Card': 'K', 'Color': 'Spades', 'Power' : 10},
        {'Card': 'Q', 'Color': 'Spades', 'Power' : 10},
        {'Card': 'J', 'Color': 'Spades', 'Power' : 10},
        {'Card': '10', 'Color': 'Spades', 'Power' : 10},
        {'Card': '9', 'Color': 'Spades', 'Power' : 9},
        {'Card': '8', 'Color': 'Spades', 'Power' : 8},
        {'Card': '7', 'Color': 'Spades', 'Power' : 7},
        {'Card': '6', 'Color': 'Spades', 'Power' : 6},
        {'Card': '5', 'Color': 'Spades', 'Power' : 5},
        {'Card': '4', 'Color': 'Spades', 'Power' : 4},
        {'Card': '3', 'Color': 'Spades', 'Power' : 3},
        {'Card': '2', 'Color': 'Spades', 'Power' : 2},
        {'Card': 'A', 'Color': 'Diamonds', 'Power' : 11},
        {'Card': 'K', 'Color': 'Diamonds', 'Power' : 10},
        {'Card': 'Q', 'Color': 'Diamonds', 'Power' : 10},
        {'Card': 'J', 'Color': 'Diamonds', 'Power' : 10},
        {'Card': '10', 'Color': 'Diamonds', 'Power' : 10},
        {'Card': '9', 'Color': 'Diamonds', 'Power' : 9},
        {'Card': '8', 'Color': 'Diamonds', 'Power' : 8},
        {'Card': '7', 'Color': 'Diamonds', 'Power' : 7},
        {'Card': '6', 'Color': 'Diamonds', 'Power' : 6},
        {'Card': '5', 'Color': 'Diamonds', 'Power' : 5},
        {'Card': '4', 'Color': 'Diamonds', 'Power' : 4},
        {'Card': '3', 'Color': 'Diamonds', 'Power' : 3},
        {'Card': '2', 'Color': 'Diamonds', 'Power' : 2},
        {'Card': 'A', 'Color': 'Clubs', 'Power' : 11},
        {'Card': 'K', 'Color': 'Clubs', 'Power' : 10},
        {'Card': 'Q', 'Color': 'Clubs', 'Power' : 10},
        {'Card': 'J', 'Color': 'Clubs', 'Power' : 10},
        {'Card': '10', 'Color': 'Clubs', 'Power' : 10},
        {'Card': '9', 'Color': 'Clubs', 'Power' : 9},
        {'Card': '8', 'Color': 'Clubs', 'Power' : 8},
        {'Card': '7', 'Color': 'Clubs', 'Power' : 7},
        {'Card': '6', 'Color': 'Clubs', 'Power' : 6},
        {'Card': '5', 'Color': 'Clubs', 'Power' : 5},
        {'Card': '4', 'Color': 'Clubs', 'Power' : 4},
        {'Card': '3', 'Color': 'Clubs', 'Power' : 3},
        {'Card': '2', 'Color': 'Clubs', 'Power' : 2},
        {'Card': 'A', 'Color': 'Hearts', 'Power' : 11},
        {'Card': 'K', 'Color': 'Hearts', 'Power' : 10},
        {'Card': 'Q', 'Color': 'Hearts', 'Power' : 10},
        {'Card': 'J', 'Color': 'Hearts', 'Power' : 10},
        {'Card': '10', 'Color': 'Hearts', 'Power' : 10},
        {'Card': '9', 'Color': 'Hearts', 'Power' : 9},
        {'Card': '8', 'Color': 'Hearts', 'Power' : 8},
        {'Card': '7', 'Color': 'Hearts', 'Power' : 7},
        {'Card': '6', 'Color': 'Hearts', 'Power' : 6},
        {'Card': '5', 'Color': 'Hearts', 'Power' : 5},
        {'Card': '4', 'Color': 'Hearts', 'Power' : 4},
        {'Card': '3', 'Color': 'Hearts', 'Power' : 3},
        {'Card': '2', 'Color': 'Hearts', 'Power' : 2},
        ]

class Player:
    
    def __init__(self, balance = 0, cardDeck = []):
        self.balance = balance
        self.cardDeck = cardDeck
    def getCards(self, cards):
        self.cards = cards
        self.balance = self.balance + cards['Power']     
        self.cardDeck.append(cards)
    def returnBalance(self):
        return self.balance
    def showCards(self):
        for card in self.cardDeck:
            print(card['Card'] + ' of ' + card['Color'])
    def endGame(self):
        self.cardDeck = []
        
        
'''
random.shuffle(deck)
playa = Player()
print(playa.getName())
'''

def doYouPlay():
    wantToPlay = input('Do yo want to play a game?(yes/no) ') 
    
    
    if wantToPlay.lower() == 'yes':
        print(PlayGame())
    else:
        print('End of game')
        print(doYouPlay())
    
    


 
def PlayGame():
    Player1 = Player()
    comp = Player()
    Player1.endGame()
    comp.endGame()
    newDeck = deck.copy()
    random.shuffle(newDeck)
    Player1.getCards(newDeck.pop())
    comp.getCards(newDeck.pop())
    
    def printPlayer(player,name):
        print('\n')
        print(name)
        print('-------------------------------')
        print('{} cards are:'.format(name))
        player.showCards()
        print('-------------------------------')
        print('{} has '.format(name) + str(player.returnBalance()) + ' points' )
    
    while Player1.returnBalance() < 21:
        printPlayer(Player1,'Player1')
        
        cardInput = input('Do you want another card? Write "yes" or "no" ')
        if cardInput.lower() == "yes": 
            Player1.getCards(newDeck.pop())
            if Player1.returnBalance() > 21:
                printPlayer(Player1,'Player')
                print('Over 21 ! Player1 lost')
                doYouPlay()
            elif Player1.returnBalance() == 21:
                printPlayer(Player1,'Player')
                print('Player1 won !!' )
                doYouPlay()
            else:
                continue
        else:
            while comp.returnBalance() < 21:
                comp.getCards(newDeck.pop())
                if comp.returnBalance() < Player1.returnBalance():
                    printPlayer(comp,'Computer')
                    print('Player1 won!')
                    continue
                elif comp.returnBalance() > 21:
                    printPlayer(comp,'Computer')
                    print('Over 21. Computer lost. Player1 Win')
                    break
                elif comp.returnBalance() > Player1.returnBalance():
                    printPlayer(comp,'Computer')
                    print('Computer Won !!!')
                    break
                elif comp.returnBalance() < Player1.returnBalance():
                    printPlayer(comp,'Computer')
                    print('Player1 Won !!!')
                    break
                else:
                    printPlayer(comp,'Computer')
                    print('No one won!!!')
                    break
            doYouPlay()

doYouPlay()