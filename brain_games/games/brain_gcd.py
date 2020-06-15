"""Game: Greatest Common Divisor."""

import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

# Numbers range
START, STOP = 1, 100


def _get_correct_answer(n1, n2):
    """Find greatest common divisor.

    Args:
        n1: first number
        n2: second number

    Returns:
        str
    """
    if n2 == 0:
        return str(n1)
    return str(_get_correct_answer(n2, n1 % n2))


def get_question_and_answer():
    """Generate question and correct answer.

    Generate two number and get correct answer

    Returns:
        str
        str
    """
    number1 = random.randint(START, STOP)
    number2 = random.randint(START, STOP)
    correct_answer = _get_correct_answer(number1, number2)
    question = 'Question: {n1} {n2}'.format(
        n1=number1,
        n2=number2,
    )
    return question, correct_answer
