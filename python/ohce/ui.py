from ohce import reverse


class ConsoleInteractor:
    def read_input(self):
        return input()

    def print_message(self, message):
        print(message)


class UI:
    def __init__(self):
        self.interactor = ConsoleInteractor()

    def main_loop(self):
        while True:
            text = input("> ")
            if text.lower() == "quit":
                break
            print(text[::-1])
            if text.lower() == text[::-1].lower():
                print("That was a palindrome!")
