"""Game: Prime Number."""

import random

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. '
    + 'Otherwise answer "no".'
)

# Numbers range
START, STOP = 1, 100

# String representations for answers
PRIME_ANSWER = 'yes'
NOT_PRIME_ANSWER = 'no'


def _get_correct_answer(target):
    """Return string representation for correct answer.

    Args:
        target: target number

    Returns:
        str
    """
    divisor = 2
    while divisor < target:
        if (target % divisor) == 0:
            return NOT_PRIME_ANSWER
        divisor += 1
    return PRIME_ANSWER


def get_description():
    """Return game description.

    Returns:
        str
    """
    return GAME_DESCRIPTION


def set_up():
    """Generate question and correct_answer.

    Generate target number, get correct answer for the target number
    and generate question itself

    Returns:
        str
        str
    """
    target = random.randint(START, STOP)
    correct_answer = _get_correct_answer(target)
    question = '{target}'.format(target=target)

    return question, correct_answer
