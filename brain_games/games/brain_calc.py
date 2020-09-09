"""Game: Calculator."""

import random

GAME_DESCRIPTION = 'What is the result of the expression?'

# Numbers range
START, STOP = 1, 100

# Arithmetical operators to be used in game
ADDITION = '+'
SUBTRACTION = '-'
MULTIPLICATION = '*'


def _calculate(operand_x, operand_y, operator):
    """Calculate correct answer.

    Args:
        operand_x: first operand
        operand_y: second operand
        operator: operator for provided operands

    Returns:
        int
    """
    number = None
    if operator == ADDITION:
        number = operand_x + operand_y
    elif operator == SUBTRACTION:
        number = operand_x - operand_y
    elif operator == MULTIPLICATION:
        number = operand_x * operand_y
    return number


def get_description():
    """Return game description.

    Returns:
        str
    """
    return GAME_DESCRIPTION


def set_up():
    """Generate question and correct answer.

    Generate operands and operator, calculate correct answer
    and generate question itself

    Returns:
        str
        str
    """
    operator = random.choice([ADDITION, SUBTRACTION, MULTIPLICATION])
    operand_x = random.randint(START, STOP)
    operand_y = random.randint(START, STOP)
    correct_answer = str(_calculate(operand_x, operand_y, operator))
    question = '{x} {operator} {y}'.format(
        x=operand_x,
        operator=operator,
        y=operand_y,
    )
    return question, correct_answer
