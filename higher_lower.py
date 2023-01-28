import random

class Game():
    def __init__(self):
        self.start = 1
        self.end = 10
        self.guess_limit = 5
        self.guess_ct = 0
        self.won = False
        self.target = None
        self.feature_map = {
            'G': self.modify_guess_limit,
            'R': self.modify_range,
            'D': self.reset,
            'C': self.play_game
        }
        self.main_screen()

    def main_screen(self):
        change_request = None
        while change_request != 'C':
            print()
            change_request = input("Please press the key representing any of the following settings that you would like to change: Guess limit (G), Guess range (R), Reset all features to defaults (D), or Continue (C): ")
            self.feature_map[change_request]()

    def reset(self):
        self.start = 1
        self.end = 10
        self.guess_limit = 5
        
    def modify_range(self):
        # provide user with more info and opportunity to back out
        print()
        print("This feature allows you to modify the range of values that the secret number can be between.")
        validate = input("Please press 'D' if you would like to reset the range to its default or 'E' if you would like to exit and keep the current setting as is; otherwise, please press any other key to continue: ")
        if validate == 'D':
            self.start = 1
            self.end = 10
            return
        elif validate == 'E':
            return
        # prompt the user to specify a number range
        self.start = int(input("Please enter the start of the range. (For example, if you wanted the range of valid numbers to be between 10 and 30, you would enter '10'): "))
        self.end = int(input("Please enter the end of the range. (For example, if you wanted the range of valid numbers to be between 10 and 30, you would enter '30'): "))

    def generate_target(self):
        self.target = random.randint(self.start, self.end)

    def modify_guess_limit(self):
        print()
        print("This feature allows you to modify the number of attempts you have to guess the secret number.")
        validate = input("Please press 'D' if you would like to reset the guess limit to its default or 'E' if you would like to exit and keep the current setting as is; otherwise, please press any other key to continue: ")
        if validate == 'D':
            self.guess_limit = 5
            return
        elif validate == 'E':
            return
        # prompt the user to specify guess limit
        print("")
        self.guess_limit = int(input("Great! What is the maximum number of guesses you’d like to specify? Please enter a numerical value. (For example, if you wanted to have up to 5 guesses before the game ends, you would enter '5'): "))

    def play_game(self):
        print()
        # validate user is ready to play game
        confirmation = input("Are you ready to start the game? (Y/N): ")
        if confirmation == 'N':
            self.main_screen()
            return

        self.generate_target()
        # generate a random number between number range
        while self.guess_ct < self.guess_limit and not self.won:
        # prompt user for guess and based on guess, provide
            guess = int(input("Guess the number: "))
            self.guess_ct += 1
            if guess == self.target:
                print("Correct! You guessed the number.")
                self.won = True
                break
            elif guess < self.target:
                # update guess ct and provide feedback
                print(f"Too low! Try again. You have {self.guess_limit - self.guess_ct} guesses remaining.")
            elif guess > self.target:
                print(f"Too high! Try again. You have {self.guess_limit - self.guess_ct} guesses remaining.")
            
        # if game won, print won
        if self.won:
            print(f"Congrats! You won the game in {self.guess_ct} guesses!")
        # if game not won after reaching guess limit, print loss
        else:
            print(f"Sorry, you've ran out of guesses.")
        # prompt user to play another game
        play_again = input("Would you like to play again? (Y/N): ")
        if play_again == 'Y':
            self.won = False
            self.guess_ct = 0
            self.play_game()

def main():
    print('run')
    game = Game()
    # game.play_game()

if __name__ == "__main__":
    main()