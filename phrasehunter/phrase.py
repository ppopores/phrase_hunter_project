# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses or letter == " ":
                print(f"{letter} ", end=" ")
            else:
                print(f"_ ", end=" ")

    def check_guess(self, user_guess):
        return user_guess in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True