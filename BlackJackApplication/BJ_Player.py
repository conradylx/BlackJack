from BlackJackApplication import Games
from BlackJackApplication.BJ_Hand import BJ_Hand


class BJ_Player(BJ_Hand):

    def __init__(self, name, bet=0, money=100):
        super().__init__(name)
        self.bet = bet
        self.money = money

    def set_bet_amount(self):
        while True:
            try:
                self.bet = int(input('How much money do you want to bet?: '))
                if self.bet > self.money:
                    print('You dont have that much money')
                    continue
            except ValueError:
                print("You need to enter numeric format of amount")
                continue
            else:
                break

    def is_hitting(self):
        response = Games.ask_yes_or_no('\n' + self.name + ', do you want to pick a card? (T/N): ')
        return response == 't'

    def bust(self):
        print(self.name, 'busts.')
        self.lose(self.bet)

    def lose(self, win_amount):
        print(self.name, 'lose')
        self.money -= win_amount

    def win(self, win_amount):
        print(self.name, 'wins')
        self.money += win_amount

    def push(self):
        print(self.name, 'draws')

    def set_betting_amount(self):
        while True:
            try:
                self.bet = int(
                    input(f"{self.name} how much is your bet? (1-{self.money}): ")
                )
                if self.bet > self.money:
                    print("You don't have enough funds!")
                    continue
            except ValueError:
                print("You need to enter a valid number!")
                continue
            else:
                break
