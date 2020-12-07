
"""Welcome user."""


import random

import prompt


def is_current_answer(answer, question):
    """Welcome user question.

    Parameters:
        answer: round game
        question: count.

    Returns:
        answer_good_yes: yes or no
        answer_good_no: yes or no
    """

    answer_yes = 'yes'
    answer_no = 'no'
    answer_good_yes = answer == answer_yes and question % 2 == 0
    answer_good_no = answer == answer_no and question % 2 != 0

    return answer_good_yes or answer_good_no


def ask_question(round_of_game, count_of_round):
    """Welcome user question.

    Parameters:
        round_of_game: round game
        count_of_round: count.
    """

    while round_of_game < count_of_round:
        question = random.randint(1, 1000)
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if is_current_answer(answer, question):
            print('Correct!')
            round_of_game += 1
        else:
            break


def start_game(name_user):
    """Welcome user question.

    Parameters:
        name_user: round game
    """

    print('Answer "yes" if the number is even, otherwise answer "no".')
    round_of_game = 1
    count_of_round = 3
    ask_question(round_of_game, count_of_round)
    if round_of_game < count_of_round:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {0}!".format(name_user))
    else:
        print('Congratulations, {0}!'.format(name_user))
