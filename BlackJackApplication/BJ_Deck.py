from BlackJackApplication.BJ_Card import BJ_Card
from BlackJackApplication.Deck import Deck


class BJ_Deck(Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
