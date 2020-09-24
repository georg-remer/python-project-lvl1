"""Game: Calculator."""

import operator as operator_module
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

    Raises:
        ValueError: unknown operator is passed
    """
    if operator == ADDITION:
        return operator_module.add(operand_x, operand_y)
    if operator == SUBTRACTION:
        return operator_module.sub(operand_x, operand_y)
    if operator == MULTIPLICATION:
        return operator_module.mul(operand_x, operand_y)
    raise ValueError("Unknown operator: '{operator}''".format(
        operator=operator,
    ))


def get_question_with_answer():
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
