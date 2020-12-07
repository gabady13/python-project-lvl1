#!/usr/bin/env python

"""welcome user."""


import brain_games
from games import even


def main():
    """Welcome user function."""
    name = brain_games.main()
    even.start_game(name)


if __name__ == '__main__':
    main()
