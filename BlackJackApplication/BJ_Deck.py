from BlackJackApplication.BJ_Card import BJ_Card
from BlackJackApplication.Deck import Deck


class BJ_Deck(Deck):
    def populate(self):
        counter = 0
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
                counter += 1
        return counter


if __name__ == '__main__':
    cards = BJ_Deck()
    print(cards.populate())
