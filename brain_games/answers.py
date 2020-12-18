"""Play games."""

from brain_games import constants

TYPE_OF_GAMES = constants.TYPE_GAMES
REPRESENTATION = 'REPRESENTATION'
VAL = 'VALUE'


def gcd(one_number, two_number):
    """Find NOD of numbers.

    Parameters:
        one_number: numeric of NOD
        two_number: numeric of NOD

    Returns:
        result: NOD
    """
    while one_number != 0 and two_number != 0:
        if one_number > two_number:
            one_number %= two_number
        else:
            two_number %= one_number

    return one_number + two_number


def get_correct_answer(game, question):
    """Get answer of game.

    Parameters:
        question: question
        game: name game

    Returns:
        answer: correct answer
    """
    answer = None

    if game is TYPE_OF_GAMES.even:
        if question[REPRESENTATION] % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
    elif game is TYPE_OF_GAMES.calc:
        answer = str(eval(question[REPRESENTATION]))
    elif game is TYPE_OF_GAMES.gcd:
        num_one = question[VAL][0]
        num_two = question[VAL][1]
        answer = str(gcd(num_one, num_two))
    elif game is TYPE_OF_GAMES.progression:
        answer = question[VAL]

    return answer
