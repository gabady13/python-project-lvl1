
"""Welcome user returns name user."""

import prompt


def welcome_user():
    """Do welcome and return user name.

    Returns:
        name: yes or

    """

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
