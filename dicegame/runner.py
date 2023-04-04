from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:
    """
    Hosts games of Sum the Dice.

    Attributes:
        round: An integer indicating the current round.
        wins: An integer indicating how many times the user has won in total.
        losses: An integer indicating how many times the user has lost in total.
        c: An integer indicating the number of consecutive wins the user has
           right now.
    """

    # Constants
    N_DICE = 5          # Number of dice to roll
    N_TO_WIN = 6        # Consecutive wins required to win

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all variables to 0."""
        self.round = 1
        self.wins = 0
        self.losses = 0
        self.c = 0
        self.roll()

    def roll(self):
        self.dice = Die.create_dice(self.N_DICE)

    def answer(self):
        """Returns the current accurate dice sum."""
        total = 0
        for die in self.dice:
            total += die.value
        return total
    
    def play_round(self):
        """Rolls one set of dice and ask for results.
        Requires user input of an integer."""
        self.roll()

        for die in self.dice:
            print(die.show())

        # TODO (XS - 4/4/23) can't handle a non-int guess
        guess = input("What is your guess?: ")
        guess = int(guess)

        if guess == self.answer():
            print("Correct!")
            self.wins += 1
            self.c += 1

        else:
            print("Sorry, that's wrong.")
            print("The answer is: {}".format(self.answer()))
            self.losses += 1
            self.c = 0

    def run(self):
        # Runs the game from the GameRunner class.
        self.reset()
        
        while True:
            print("Round {}\n".format(self.round))
            self.play_round()

            print("Wins: {} Losses {}".format(self.wins, self.losses))
            self.round += 1

            if self.c == self.N_TO_WIN:
                print("You won! Congrats!")
                break

            # Prompt until users give a y or n response (blank means yes)
            prompt = input("Would you like to play again? [Y/n]: ")

            while prompt[:1].lower() not in ('y', 'n', ''):
                prompt = input("Would you like to play again? [Y/n]: ")
            
            if prompt[:1].lower() == 'n':
                print("Goodbye!")
                break