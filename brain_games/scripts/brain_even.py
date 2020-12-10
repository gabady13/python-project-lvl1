#!/usr/bin/env python

"""Init of game."""

import play_game
import constants


def main():
    """Init game."""
    play_game.start_game(constants.TYPE_GAMES.even)


if __name__ == '__main__':
    main()
