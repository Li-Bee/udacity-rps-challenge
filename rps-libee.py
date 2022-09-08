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

# moves = [rock, paper, scissors, fire, water, dynamite]

# dictionary
# moves_dict = {
#     rock: "rock",
#     paper: "paper",
#     scissors: "scissors",
#     fire: "fire",
#     water: "water",
#     dynamite: "dynamite"
# }

moves_dict = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors,
    "fire": fire,
    "water": water,
    "dynamite": dynamite
}

# https://bobbyhadz.com/blog/python-dict-keys-object-is-not-subscriptable
# moves_dict.keys() would return object not a list
# these objects are not subscriptable,
# we can't access them at a specific index.
# convert to a list
moves_keys = list(moves_dict.keys())  # length of 6
moves_values = list(moves_dict.values())

player_one_count = 0
player_two_count = 0


class Player:

    def __init__(self):
        # set the my_move and their_move to none when create player object
        self.my_move = None
        self.their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


# Computer player - subclass of player
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves_values)


# Human player - subclass of player
class HumanPlayer(Player):
    def move(self):
        human_choice = valid_input(
            "Choose rock, paper, scissors, dynamite, fire or water\n",
            moves_keys)
        return moves_dict[human_choice]

# Computer player - always plays rock - subclass of player


class RockPlayer(Player):
    def move(self):
        return moves_dict["rock"]

# ReflectPlayer and CyclePlayer adapted from:
# https://github.com/drodriguezmtb/Rock-Paper-Scissors-Udacity/blob/master/python-final-project.py


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        # store the moves of the players
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        # if not played first round yet
        # then random move as not stored a move yet
        if self.their_move is None:
            return random.choice(moves_values)
        else:
            return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        # store the moves of the players
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        # if not played first round yet
        # then random move as not stored a move yet
        if self.my_move is None:
            return random.choice(moves_values)
        else:
            # index() gives value of the index
            move_index = moves_values.index(self.my_move) + 1
            # give len of 6
            if move_index == len(moves_values):
                # if reached limit of index reset back to zero
                move_index = 0
            return moves_values[move_index]


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
    def __init__(self, playerone, playertwo):
        # players who are playing the game
        self.player_one = playerone
        self.player_two = playertwo
        # set the round counter to nil at start of the game
        self.player_one_count = 0
        self.player_two_count = 0

    def play_round(self):
        player_one_move = self.player_one.move()
        player_two_move = self.player_two.move()
        print(
            f"Player 1 chose: {player_one_move} "
            f"Player 2 chose: {player_two_move}")

        if tie(player_one_move, player_two_move) is True:
            print(f"It is a tie!")
            self.player_one_count += 1
            self.player_two_count += 1
        elif beats(player_one_move, player_two_move) is True:
            print(f"Player 1 is the winner!")
            self.player_one_count += 1
        else:
            print(f"Player 2 is the winner!")
            self.player_two_count += 1
        print(
            f"Player 1 score:{self.player_one_count} vs "
            f"Player 2 score:{self.player_two_count}")

        # saves moves
        self.player_one.learn(player_one_move, player_two_move)
        self.player_two.learn(player_two_move, player_one_move)

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
        if self.player_one_count > self.player_two_count:
            print("Player 1 wins the match. ")
            print(
                f"Player 1 score:{self.player_one_count} vs "
                f"Player 2 score:{self.player_two_count}")
        elif self.player_one_count == self.player_two_count:
            print("It's a tie!")
            print(
                f"Player 1 score:{self.player_one_count} vs "
                f"Player 2 score:{self.player_two_count}")
        else:
            print("Player 2 wins the match.")
            print(
                f"Player 1 score:{self.player_one_count} vs "
                f"Player 2 score:{self.player_two_count}")

# Choice of opponent adapted from:
# https://github.com/drodriguezmtb/Rock-Paper-Scissors-Udacity/blob/master/python-final-project.py


if __name__ == '__main__':

    # select opponent
    opponent_players = {
        "human": HumanPlayer(),
        "computer": RandomPlayer(),
        "cycler": CyclePlayer(),
        "reflector": ReflectPlayer(),
        "rock it": RockPlayer(),
    }

    choose = valid_input(
        f"Choose your contender: human, computer, cycler,"
        f"reflector or rock it\n",
        opponent_players.keys()).lower()
    if choose in opponent_players.keys():
        game = Game(HumanPlayer(), opponent_players[choose])
        game.play_game()
    else:
        print(f"Please select a player on the list."
              f"You have chosen one that does not exist yet!")
