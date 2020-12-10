
"""Welcome user."""

from games import constants, play_game


def init_game():
    """Initialize game even."""
    play_game.start_game(constants.TYPE_GAMES.even)
