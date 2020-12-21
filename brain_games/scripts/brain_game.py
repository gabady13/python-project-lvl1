#!/usr/bin/env python

"""welcome user."""

from brain_games import cli


def main():
    """Welcome function.

    Returns:
        name: name of user
    """
    print('Welcome to the Brain Games!')

    return cli.get_name_user()


if __name__ == '__main__':
    main()
