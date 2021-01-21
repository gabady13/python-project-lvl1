#!/usr/bin/env python

"""Init of game."""

from brain_games import engine_game, games


def main():
    """Init game."""
    engine_game.start_game(games.gcd)


if __name__ == '__main__':
    main()
