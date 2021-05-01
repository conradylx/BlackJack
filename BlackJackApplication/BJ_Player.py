from BlackJackApplication import Games
from BlackJackApplication.BJ_Hand import BJ_Hand


class BJ_Player(BJ_Hand):

    def is_hitting(self):
        response = Games.ask_yes_or_no('\n' + self.name + ', do you want to pick a card? (T/N): ')
        return response == 't'

    def bust(self):
        print(self.name, 'busts.')
        self.lose()

    def lose(self):
        print(self.name, 'lose')

    def win(self):
        print(self.name, 'wins')

    def push(self):
        print(self.name, 'draws')
