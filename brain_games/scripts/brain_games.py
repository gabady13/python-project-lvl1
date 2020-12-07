#!/usr/bin/env python

"""welcome user."""

from cli import welcome_user


def main():
    """Welcome user function.

    Returns:
        name: yes or no
    """

    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == '__main__':
    main()
