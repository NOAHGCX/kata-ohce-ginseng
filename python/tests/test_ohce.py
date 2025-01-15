import pytest
from ohce.greeter import Greeter, FakeClock
from ohce.ui import UI

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


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    for hour in range(24):
        # Arrange
        clock = FakeClock(hour)
        greeter = Greeter(clock)
        
        # Act
        result = greeter.greet()
        
        # Assert
        assert result is not None
        
        



def test_ohce_main_loop(capsys):
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
    ui = UI()  
    
    # Act
    ui.process_input("hello")  
    ui.process_input("oto")
    
    # Assert
    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.split('\n') if line.strip()]
    
    assert len(output_lines) >= 3
    assert output_lines[0] == 'olleh'
    assert output_lines[1] == 'oto'
    assert output_lines[2] == 'That was a palindrome!'
