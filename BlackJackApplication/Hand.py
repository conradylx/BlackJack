from BlackJackApplication.Cards import Card


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


if __name__ == '__main__':
    card1 = Card('A', '♦')
    print('Show card objects:')
    print(card1)
    card2 = Card('2', '♦')
    card3 = Card('3', '♦')
    card4 = Card('4', '♦')
    card5 = Card('5', '♦')
    print('Show other card objects:')
    print(card2, card3, card4, card5)

    my_hand = Hand()
    print('Show cards in my hand before taking any other cards:')
    print(my_hand)
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    print('Show cards after taking 5 cards:')
    print(my_hand)

    your_hand = Hand()
    my_hand.give(card1, your_hand)
    my_hand.give(card2, your_hand)
    print('Show two first cards given to you.')
    print('Your hand: ', your_hand)
    print('My hand: ', my_hand)
    my_hand.clear()
    print('My hand after taking all the cards:')
    print(my_hand)
