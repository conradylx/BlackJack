from BlackJackApplication.Cards import Card
from BlackJackApplication.Positionable_Card import Positionable_Card
from BlackJackApplication.Unprintable_card import Unprintable_card

if __name__ == '__main__':
    card1 = Card('A', '♥')
    card2 = Unprintable_card('A', '♠')
    card3 = Positionable_Card('A', '♦')
    print('Show objects of class Card:')
    print(card1)
    print('Show unprintable card:')
    print(card2)
    print('Show positionable card:')
    print(card3)
    print('Change state of positionable card:')
    card3.flip()
    print('Show positionable card')
    print(card3)