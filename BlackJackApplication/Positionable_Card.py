from BlackJackApplication.Cards import Card
from Unprintable_card import Unprintable_card


class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        # super(Positionable_Card, self).__init__(rank, suit) # Useful if there's more than one class inheritance
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


if __name__ == '__main__':
    pass
