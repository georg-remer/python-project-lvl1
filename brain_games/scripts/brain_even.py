"""Game logic."""

import random

from brain_games.cli import ask_for_answer, welcome_user
from brain_games.scripts.brain_games import get_intro

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
NR_QUESTIONS = 3
EVEN_ANSWER = 'yes'
NOT_EVEN_ANSWER = 'no'
CORRECT = 'Correct!'


def get_game_description():
    """Return game description.

    Returns:
        str
    """
    return GAME_DESCRIPTION


def get_correct_answer(is_even=False):
    """Return string representation for correct answer.

    Args:
        is_even: flag for even

    Returns:
        str
    """
    if is_even:
        return EVEN_ANSWER
    return NOT_EVEN_ANSWER


def get_opposite_answer(answer):
    """Return opposite answer.

    Return 'yes' if 'no' was provided and vice versa.

    Args:
        answer: 'yes' or 'no'

    Returns:
        str
    """
    if answer not in set(EVEN_ANSWER, NOT_EVEN_ANSWER):
        return 'Such an answer is not specified!'
    if answer == EVEN_ANSWER:
        return NOT_EVEN_ANSWER
    if answer == NOT_EVEN_ANSWER:
        return EVEN_ANSWER


def get_question():
    """Generate question.

    Generate target number, set 'is_even' to True if target number is even,
    define correct answer for the target number and generate question itself

    Returns:
        str
        str
    """
    target = random.randint(1, 100)
    is_even = bool(target % 2 == 0)
    correct_answer = get_correct_answer(is_even)
    question = 'Question: {target}'.format(target=target)

    return question, correct_answer


def play_game(user_name):
    """Play the game.

    Args:
        user_name: user name to make the game personalized

    Play the game until number of successful attempts reaches
    the number of questions or till first wrong answer is provided
    """
    for _ in range(NR_QUESTIONS):
        (question, correct_answer) = get_question()
        print(question)
        user_answer = ask_for_answer()
        if user_answer == correct_answer:
            print(CORRECT)
        else:
            print(
                "'{user_answer}' is wrong answer ;(.".format(
                    user_answer=user_answer,
                )
                + "Correct answer was '{correct_answer}'.\n".format(
                    correct_answer=correct_answer,
                )
                + "Let's try again, {user_name}!".format(
                    user_name=user_name,
                ),
            )
            break
    else:
        print('Congratulations, {user_name}!'.format(user_name=user_name))


def main():
    """Print intro and game description, welcome user. Play the game."""
    print(get_intro())
    print('{description}\n'.format(description=get_game_description()))
    (greeting, user_name) = welcome_user()
    print(greeting)
    play_game(user_name)


if __name__ == '__main__':
    main()
