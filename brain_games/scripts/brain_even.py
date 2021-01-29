#!/usr/bin/env python

"""Init of game."""

from brain_games import engine, games


def main():
    """Init game."""
    engine.start_game(games.even)


if __name__ == '__main__':
    main()
