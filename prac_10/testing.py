"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return (f"{s} " * n).strip()


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence starting with a capital and ending with a single full stop.
    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("Python is cool.  ")
    'Python is cool.'
    """
    phrase = phrase.strip()

    # Capitalise first character and keep the rest same
    phrase = phrase[0].upper() + phrase[1:]

    # If the last character is a full stop then remove it
    if phrase[-1] == ".":
        phrase = phrase[:-1]

    # Add only one full stop
    phrase = phrase + "."
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    car = Car(fuel=10)
    car.drive(3)
    assert car.fuel == 7, "Fuel should decrease after driving"

    car = Car()
    assert car.fuel == 0, "Starting fuel should be 0"

    car2 = Car(20)
    assert car2.fuel == 20, "New fuel should be set correctly"


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# (Don't change the tests, change the function!)

# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
#   'hello' -> 'Hello.'
#   'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.
