import pygame
from enum import Enum
from enum import IntEnum

deck = [[],[]]
cardactionvalue = []
cardCostvalue = []

deck2 = deck[1]
deck1 = deck[0]


class cardActVal:
    strikeDMG = 6
    defendDFD = 5

class cardCost:
    strikeCST = 1
    defendCST = 1
   
        
cardactionvalue.append(cardActVal.strikeDMG)
cardactionvalue.append(cardActVal.defendDFD)
cardCostvalue.append(cardCost.strikeCST)
cardCostvalue.append(cardCost.defendCST)

#Appends my cost and action values to one array to sort from
for i in range(len(cardactionvalue)-1):
    deck1.append(cardactionvalue[i])
    deck2.append(cardCostvalue[i])
    deck1.append(cardactionvalue[i+1])
    deck2.append(cardCostvalue[i+1])

#Saves the data for the strike card in an array
class STRIKE:
    def strike():
        Strike = []
        Strike.append(deck1[0])
        Strike.append(deck2[0])
        return Strike

#Saves the data for the defend card in an array
class DEFEND:
    def defend():
        Defend = []
        Defend.append(deck1[1])
        Defend.append(deck2[1])
        return Defend

attack = []  
attack = STRIKE.strike()

shield = []
shield = DEFEND.defend()


#Card Positions
W = 100
H = 400

base_energy = 3



