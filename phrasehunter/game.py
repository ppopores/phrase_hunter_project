# Create your Game class logic in here.
import random

from phrasehunter.phrase import Phrase
from phrasehunter.phrase_bank import phrase_bank_tv

class Game:
    def __init__(self):
        self.missed = 0
        self.show_name = random.choice(list(phrase_bank_tv.keys()))
        self.phrases = [Phrase(item) for item in phrase_bank_tv[self.show_name]]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = [" "]

    def welcome(self):
        if (len(str(self.active_phrase)) * 2) < 58:
            window_length = 58
        else:
            window_length = int(len(str(self.active_phrase)) * 1.5)
        print("="*window_length)
        print(" |"*(int(window_length/2)))
        print("="*window_length)
        message = f"Welcome to Hangman, No Gallows"
        print(" " * int((window_length-len(message))/2) + message)
        message2 = f"{self.show_name} Edition"
        print(" " * int((window_length-len(message2))/2) + message2)
        print("="*window_length)


    def get_guess(self):
        self.user_guess = input(f"\n\nGuess a letter:        ")
        self.user_guess = self.user_guess.lower()
        if len(self.user_guess) != 1:
            print("Please one letter at a time.")
        elif self.user_guess.isdigit():
            print("Please use a letter; just one letter!")
        else:
            return


    def game_over(self):
        if self.missed == 5:
            print("\nSadly, you have lost this round.")
        else:
            print("\nWhoa! You guessed correctly!")

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nNumber Missed: {self.missed}\n")
            self.active_phrase.display(self.guesses)
            self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1
        self.game_over()

    def play_again(self):
        while True:
            self.again = input("\nWould you like to play again? Y/N  \n")
            if self.again.lower() == "y":
                print("\n")
                self.game = Game()
                self.game.start()
            else:
                print("\nSmell ya later!")
                break










