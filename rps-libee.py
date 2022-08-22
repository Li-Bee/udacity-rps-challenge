import emoji
import random
import time

# emoji aliases from: https://unicode.org/emoji/charts/full-emoji-list.html
# how to use: https://pypi.org/project/emoji/
rock = emoji.emojize(":rock:")
paper = emoji.emojize(":scroll:")
scissors = emoji.emojize(":scissors:")
fire = emoji.emojize(":fire:")
water = emoji.emojize(":water_wave:")
dynamite = emoji.emojize(":firecracker:")

moves = [rock, paper, scissors, fire, water, dynamite]

player_one_count = 0
player_two_count = 0


class Player:
    def move(self):
        pass


# Computer player - subclass of player
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human player - subclass of player
class HumanPlayer(Player):
    def move(self):
        human_choice = valid_input(
            "Choose rock, paper, scissors, dynamite, fire or water\n", moves)
        return human_choice


# valid input - string function
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f"Sorry, the option {option} is invalid. "
              "Please try again.")


# which move beats the other move
def beats(one, two):
    return ((one == rock and two == scissors) or
            (one == scissors and two == paper) or
            (one == paper and two == rock) or
            (one == dynamite and two == rock) or
            (one == fire and two == paper) or
            (one == water and two == fire)
            )


# returns True if there is a tie
def tie(one, two):
    return ((one == rock and two == rock) or
            (one == scissors and two == scissors) or
            (one == paper and two == paper) or
            (one == dynamite and two == dynamite) or
            (one == fire and two == fire) or
            (one == water and two == water)
            )


class Game:

    # assign player 1 and player 2 when object created
    def __init__(self, PlayerOne, PlayerTwo):
        self.player_one = PlayerOne
        self.player_two = PlayerTwo
        self.player_one_count = 0
        self.player_two_count = 0

    def play_round(self):
        player_one_move = self.player_one.move()
        player_two_move = self.player_two.move()
        print(
            f"Player 1 chose: {player_one_move}  Player 2 chose: {player_two_move}")

        if tie(player_one_move, player_two_move) == True:
            print(f"It is a tie!")
            self.player_one_count += 1
            self.player_two_count += 1
        elif beats(player_one_move, player_two_move) == True:
            print(f"Player 1 is the winner!")
            self.player_one_count += 1
        else:
            print(f"Player 2 is the winner!")
            self.player_two_count += 1
        print(
            f"Player 1 score:{self.player_one_count} vs Player 2 score:{self.player_two_count}")

    def play_game(self):
        # countdown to start game
        n = 3
        while n > 0:
            print(n)
            # pauses python for 1s, so more like countdown
            time.sleep(1)
            n -= 1

        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            time.sleep(1)
            self.play_round()
            time.sleep(1)
        print("Game over!")


if __name__ == '__main__':
    # play human aganst computer
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
