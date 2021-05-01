import random

from Cards import Card
from Hand import Hand


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Cannot continue, out of cards")


if __name__ == '__main__':
    deck1 = Deck()
    print('Created new deck of cards.')
    print('Deck of cards:')
    print(deck1)
    deck1.populate()
    print('Deck of cards has been populated.')
    print('Deck of cards:')
    print(deck1)
    print('Shuffle deck.')
    deck1.shuffle()
    print(deck1)
    my_hand = Hand()
    your_hand = Hand()
    hands = [my_hand, your_hand]
    deck1.deal(hands, per_hand=5)
    print('Show hands:')
    print(f'My hand: {my_hand}, Your hand: {your_hand}')
    deck1.clear()
    print('Deck cards:', deck1)