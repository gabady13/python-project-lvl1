"""Constants of the games."""

from enum import Enum
from typing import Any, Union

TYPE_GAMES: Union[Union[type, Enum], Any] = Enum('game', 'even,calc,gcd,progression,prime')
