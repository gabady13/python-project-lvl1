"""Returns types of games."""

from enum import Enum


def type_of_games():
    """Do type games.

    Returns:
        type: enum of games.

    """

    return Enum('game', 'even,calc,gcd,progression,prime')

def value_of_even():
    """Do type games.

    Returns:
        value: enum of games.

    """

    return type_of_games().even.value
