
"""Welcome user."""

from games import play_game, type_games


def init_game():
    """Initialize game even."""

    play_game.start_game(type_games.type_of_games().even)
