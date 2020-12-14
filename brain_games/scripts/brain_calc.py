#!/usr/bin/env python

"""Init of game."""

from brain_games import constants, play_game


def main():
    """Init game."""
    play_game.start_game(constants.TYPE_GAMES.calc)


if __name__ == '__main__':
    main()
