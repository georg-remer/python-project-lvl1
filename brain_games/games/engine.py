"""Game engine.

The flow is the following:
1. Print intro
2. Print game description if game is specified
3. Welcome user
4. Play the game n-rounds (or till first wrong answer) if game is specified:
4.1. Print question
4.2. Get answer from user
4.3. Check if asnwer is correct
"""

from brain_games.cli import ask_user, inform_user, welcome_user
from brain_games.games import (
    brain_calc,
    brain_even,
    brain_gcd,
    brain_progression,
)

INTRO = 'Welcome to the Brain Games!'
NUMBER_OF_ROUNDS = 3


def init(game):
    """Game initialization.

    Args:
        game: the name of the game to be played

    Returns:
        str
        function
    """
    if game == 'brain_calc':
        game_description = brain_calc.GAME_DESCRIPTION
        get_question_and_answer = brain_calc.get_question_and_answer
    elif game == 'brain_even':
        game_description = brain_even.GAME_DESCRIPTION
        get_question_and_answer = brain_even.get_question_and_answer
    elif game == 'brain_gcd':
        game_description = brain_gcd.GAME_DESCRIPTION
        get_question_and_answer = brain_gcd.get_question_and_answer
    elif game == 'brain_progression':
        game_description = brain_progression.GAME_DESCRIPTION
        get_question_and_answer = brain_progression.get_question_and_answer
    return game_description, get_question_and_answer


def play_game(game=None):
    """Game flow.

    Plays the game if specified, or just greets user

    Args:
        game: the name of the game to be played
    """
    # Print intro
    inform_user(INTRO)

    # Get game and print it's description
    if game:
        game_description, get_question_and_answer = init(game)
        inform_user(game_description)

    # Welcome user and get user name
    user_name = welcome_user()

    # Get question and correct answer, play the game
    if game:
        for _ in range(NUMBER_OF_ROUNDS):
            (question, correct_answer) = get_question_and_answer()
            inform_user(question)
            user_answer = ask_user()
            if user_answer == correct_answer:
                inform_user('Correct!')
            else:
                inform_user(
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
            inform_user('Congratulations, {user_name}!'.format(
                user_name=user_name,
            ))
