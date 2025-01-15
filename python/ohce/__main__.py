from ohce.greeter import Greeter, SystemClock
from ohce.ui import UI


def main():
    clock = SystemClock()
    greeter = Greeter(clock)
    greetings = greeter.greet()
    print(greetings)

    ui = UI()
    ui.main_loop()


if __name__ == "__main__":
    main()
