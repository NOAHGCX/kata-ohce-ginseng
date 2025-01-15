import pytest
from ohce.greeter import Greeter, FakeClock


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
        assert isinstance(result, str)
        
        # Additional assertions to verify correct greetings
        if 6 <= hour < 12:
            assert result == "Good morning"
        elif 12 <= hour <= 19:
            assert result == "Good afternoon"
        else:  # hour >= 20 or hour < 6
            assert result == "Good night"


def test_ohce_main_loop(monkeypatch, capsys):
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
    # Arrange
    inputs = ['hello', 'oto', 'quit']
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    
    # Act
    from ohce.__main__ import main
    main()
    
    # Assert
    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.split('\n') if line.strip()]
    
    assert len(output_lines) >= 4
    assert output_lines[1] == 'olleh'
    assert output_lines[2] == 'oto'
    assert output_lines[3] == 'That was a palindrome!'
