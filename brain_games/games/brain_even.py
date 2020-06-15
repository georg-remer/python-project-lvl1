"""Game: Is Even."""

import random

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'

# Numbers range
START, STOP = 1, 100

# String representations for answers
EVEN_ANSWER = 'yes'
NOT_EVEN_ANSWER = 'no'


def _get_correct_answer(target):
    """Return string representation for correct answer.

    Args:
        target: target number

    Returns:
        str
    """
    is_even = bool(target % 2 == 0)
    if is_even:
        return EVEN_ANSWER
    return NOT_EVEN_ANSWER


def get_question_and_answer():
    """Generate question and correct_answer.

    Generate target number, get correct answer for the target number
    and generate question itself

    Returns:
        str
        str
    """
    target = random.randint(START, STOP)
    correct_answer = _get_correct_answer(target)
    question = 'Question: {target}'.format(target=target)

    return question, correct_answer
