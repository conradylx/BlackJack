from Cards import Card


class Unprintable_card(Card):

    def __str__(self):
        return '<HIDDEN>'


if __name__ == '__main__':
    pass
