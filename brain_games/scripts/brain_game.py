#!/usr/bin/env python

"""welcome user."""

from brain_games import engine


def main():
    """Welcome function."""
    name = engine.ask_question(engine.WELCOME_QUESTION)
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()
