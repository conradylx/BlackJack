from BlackJackApplication.BJ_Card import BJ_Card
from BlackJackApplication.Hand import Hand


class BJ_Hand(Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = f'{self.name:<10} {super(BJ_Hand, self).__str__():>10}'
        if self.total:
            rep += f"({str(self.total)})"
            return rep
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        sum = 0
        for card in self.cards:
            sum += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and sum <= 11:
            sum += 10

        return sum

    def is_busted(self):
        return self.total > 21


if __name__ == '__main__':
    hand = BJ_Hand('Dealer')
    print(hand)
