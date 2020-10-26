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


def get_question_with_answer():
    """Generate question and correct answer.

    Generate progression and correct answer

    Returns:
        str
        str
    """
    start = random.randint(START_MIN, START_MAX)
    diff = random.randint(STEP_MIN, STEP_MAX)
    skip = random.randint(0, LENGTH - 1)

    progression = [str(start + diff * element) for element in range(LENGTH)]
    correct_answer = str(progression[skip])
    progression[skip] = '..'

    question = ' '.join(progression)
    return question, correct_answer
