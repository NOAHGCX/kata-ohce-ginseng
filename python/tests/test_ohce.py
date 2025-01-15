import pytest
from ohce.greeter import Greeter
from ohce.ui import UI

class FakeClock:
    def __init__(self, hour):
        self.hour = hour
        
    def current_hour(self):
        return self.hour

class FakeConsoleInteractor:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read_input(self):
        return self.inputs.pop(0)

    def print_message(self, message):
        self.outputs.append(message)

def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    # Arrange
    clock = FakeClock(0)
    greeter = Greeter(clock)
    
    # Act
    result = greeter.greet()
    
    # Assert
    assert result == "Good night"


@pytest.mark.parametrize("hour", range(24))
def test_greeting_never_returns_none(hour):
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    
    # Arrange
    clock = FakeClock(hour)
    greeter = Greeter(clock)
    
    # Act
    result = greeter.greet()
    
    # Assert
    assert result is not None
        

def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
    # Arrange: prepare the mock interactor with inputs and capture outputs
    inputs = ["hello", "oto", "quit"]
    expected_outputs = [
        "olleh",
        "oto",
        "That was a palindrome!"
    ]
    fake_interactor = FakeConsoleInteractor(inputs)

    # Act: run the UI main loop
    ui = UI(fake_interactor)
    ui.main_loop()

    # Assert: check the outputs
    assert fake_interactor.outputs == expected_outputs

