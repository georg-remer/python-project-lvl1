"""Game: Is Even."""

import random

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'

# Numbers range
START, STOP = 1, 100


def _is_even(number):
    """Return True if number is even else False.

    Args:
        number: number to check

    Returns:
        bool
    """
    return bool(number % 2 == 0)


def get_question_with_answer():
    """Generate question and correct_answer.

    Generate target number, get correct answer for the target number
    and generate question itself

    Returns:
        str
        str
    """
    target = random.randint(START, STOP)
    correct_answer = 'yes' if _is_even(target) else 'no'
    question = str(target)

    return question, correct_answer
