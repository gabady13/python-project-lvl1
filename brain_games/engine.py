"""Play games."""

import prompt

COUNT_ROUND = 3
WELCOME_QUESTION = 'May I have your name? '


def ask_question(text_question):
    """Ask question of user.

    Parameters:
        text_question: text of question

    Returns:
        answer: answer of user.

    """
    return prompt.string(text_question)


def start_game(game):
    """Play games.

    Parameters:
        game: module game of Brain

    """
    print('Welcome to the Brain Games!')
    print()
    name = ask_question(WELCOME_QUESTION)
    print('Hello, {0}!'.format(name))
    print(game.DESCRIPTION)
    counter = 0
    while counter < COUNT_ROUND:
        question, answer_correct = game.get_question_and_answer()
        print('Question: {0}'.format(question))
        answer_of_user = ask_question('Your answer: ')
        if answer_of_user == answer_correct:
            print('Correct!')
            counter += 1
        else:
            print("""\
'{0}' is wrong answer ;(. Correct answer was '{1}'
Let's try again, {2}!\
                """.format(answer_of_user, answer_correct, name),
                  )
            break

    else:
        print('Congratulations, {0}!'.format(name))
