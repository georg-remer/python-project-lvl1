"""Game: Brain Progression."""

import random

GAME_DESCRIPTION = 'What number is missing in the progression?'

# Progression length
LENGTH = 10

# Progression start
START_MIN = 1
START_MAX = 10

# Progression step
STEP_MIN = 1
STEP_MAX = 10


def get_question_and_answer():
    """Generate question and correct answer.

    Generate progression and correct answer

    Returns:
        str
        str
    """
    number = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    answer_position = random.randint(0, LENGTH - 1)
    correct_answer = None
    progression = ['Question:']

    for position in range(LENGTH):
        if position == answer_position:
            correct_answer = number
            progression.append('..')
        else:
            progression.append(str(number))
        number += step

    question = ' '.join(progression)
    return question, str(correct_answer)
