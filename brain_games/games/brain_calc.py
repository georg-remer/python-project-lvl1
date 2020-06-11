"""Game: Calculator."""

import random

from brain_games.cli import ask_for_answer, welcome_user
from brain_games.scripts.brain_games import get_intro

GAME_DESCRIPTION = 'What is the result of the expression?'
NR_QUESTIONS = 3
CORRECT = 'Correct!'

# Numbers range
START, STOP = 1, 100

# Arithmetical operators to be used in game
ADDITION = '+'
SUBTRACTION = '-'
MULTIPLICATION = '*'


def get_game_description():
    """Return game description.

    Returns:
        str
    """
    return GAME_DESCRIPTION


def get_correct_answer(operand_x, operand_y, operator):
    """Calculate correct answer.

    Args:
        operand_x: first operand
        operand_y: second operand
        operator: operator for provided operands

    Returns:
        str
    """
    number = None
    if operator == ADDITION:
        number = operand_x + operand_y
    elif operator == SUBTRACTION:
        number = operand_x - operand_y
    elif operator == MULTIPLICATION:
        number = operand_x * operand_y
    return str(number)


def get_question():
    """Generate question.

    Generate operands and operator, calculate correct answer
    and generate question itself

    Returns:
        str
        str
    """
    operator = random.choice([ADDITION, SUBTRACTION, MULTIPLICATION])
    operand_x = random.randint(START, STOP)
    operand_y = random.randint(START, STOP)
    correct_answer = get_correct_answer(operand_x, operand_y, operator)
    question = 'Question: {x} {operator} {y}'.format(
        x=operand_x,
        operator=operator,
        y=operand_y,
    )
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
