import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

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

def run_tests():
    """Run the tests on the functions."""
    # no message is return with assert test
    assert repeat_string("Python", 1) == "Python"
    # this should fail
    assert repeat_string("hi", 2) == "hi hi"

    # custom message with assert test, should determine Car's init method sets the odometer correctly
    # no output is needed when test is passed
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # two different ways assert statements is used to show if Car sets the fuel correctly
    # using the value passed in or the default
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('This subject rocks')
    'This subject rocks.'
    """
    # capitalise the first letter
    sentence = phrase.capitalize()
    # full stop is added when needed
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod()