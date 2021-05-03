import Games
from BlackJackApplication.BJ_Game import BJ_Game
from BlackJackApplication.Deck import Deck


def main():
    print('\t\tWelcome to Blackjack!')
    names = []
    number = Games.ask_number('Enter number of players (1-7): ', low=1, high=8)

    for i in range(number):
        name = input('Enter player name: ')
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None

    while again != 'n':
        game.play()
        game.new_deck()
        again = Games.ask_yes_or_no('\nDo you want play again? ')


if __name__ == '__main__':
    main()
