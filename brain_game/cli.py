
"""Welcome user returns name user."""

import prompt


def get_name_user():
    """Do welcome and return user name.

    Returns:
        name: name of user.

    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
