"""Game: Greatest Common Divisor."""

import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

# Numbers range
START, STOP = 1, 100


def _find_gcd(n1, n2):
    """Find greatest common divisor.

    Args:
        n1: first number
        n2: second number

    Returns:
        str
    """
    if n2 == 0:
        return n1
    return _find_gcd(n2, n1 % n2)


def get_description():
    """Return game description.

    Returns:
        str
    """
    return GAME_DESCRIPTION


def set_up():
    """Generate question and correct answer.

    Generate two number and get correct answer

    Returns:
        str
        str
    """
    number1 = random.randint(START, STOP)
    number2 = random.randint(START, STOP)
    correct_answer = str(_find_gcd(number1, number2))
    question = '{n1} {n2}'.format(
        n1=number1,
        n2=number2,
    )
    return question, correct_answer
