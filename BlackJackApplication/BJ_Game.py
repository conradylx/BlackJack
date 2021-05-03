from BlackJackApplication.BJ_Dealer import BJ_Dealer
from BlackJackApplication.BJ_Deck import BJ_Deck
from BlackJackApplication.BJ_Player import BJ_Player


class BJ_Game(object):
    def __init__(self, names):
        self.players = []

        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer('Dealer')
        self.deck = BJ_Deck()
        self.deck.populate()
        if self.deck.populate() != 52:
            print("Deck doesn't contain 52 cards.")
            quit()

        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        for player in self.players:
            if not player.is_busted():
                player.set_betting_amount()
        # noinspection PyTypeChecker
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win(player.bet)
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win(player.bet)
                    elif player.total < self.dealer.total:
                        player.lose(player.bet)
                    else:
                        player.push()
                for player in self.players:
                    player.clear()

                self.dealer.clear()
        for player in self.players:
            print(f'Total amount of {player.name}: ', player.money)
