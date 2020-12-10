
"""Welcome user."""

from games import play_game, constants


def init_game():
    """Initialize game even."""

    play_game.start_game(constants.TYPE_GAMES.even)
