"""Game: Prime Number."""

import random

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. '
    + 'Otherwise answer "no".'
)

# Numbers range
START, STOP = 1, 100


def _is_prime(number):
    """Return True if number is prime else False.

    Args:
        number: number to check

    Returns:
        bool
    """
    if number <= 1:
        return False

    divisor = 2
    while divisor < number:
        if ((number % divisor) == 0) or (divisor > (number / 2)):
            return False
        divisor += 1
    return True


def get_question_with_answer():
    """Generate question and correct_answer.

    Generate target number, get correct answer for the target number
    and generate question itself

    Returns:
        str
        str
    """
    target = random.randint(START, STOP)
    correct_answer = 'yes' if _is_prime(target) else 'no'
    question = '{target}'.format(target=target)

    return question, correct_answer
