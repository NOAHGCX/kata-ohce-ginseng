from ohce.greeter import Greeter, SystemClock
from ohce.ui import UI, ConsoleInteractor

def main():
    clock = SystemClock()
    greeter = Greeter(clock)
    greetings = greeter.greet()
    print(greetings)

    interactor = ConsoleInteractor()
    ui = UI(interactor)
    ui.main_loop()


if __name__ == "__main__":
    main()
