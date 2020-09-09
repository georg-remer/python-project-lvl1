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

from brain_games import settings
from brain_games.cli import ask_user, inform_user, welcome_user


def play(game=None):
    """Game flow.

    Plays the game if specified, or just greets user

    Args:
        game: Game module
    """
    # Print intro
    inform_user(settings.INTRO)

    # Get game setup and print it's description
    if game:
        description = game.get_description()
        inform_user('{description}\n'.format(description=description))

    # Welcome user and get user name
    user_name = welcome_user()

    # Get question and correct answer, play the game
    if game:
        for _ in range(settings.NUMBER_OF_ROUNDS):
            (question, correct_answer) = game.set_up()
            inform_user('{phrase}: {question}'.format(
                phrase=settings.QUESTION,
                question=question,
            ))
            user_answer = ask_user()
            if user_answer == correct_answer:
                inform_user('{phrase}'.format(phrase=settings.CASE_CORRECT))
            else:
                inform_user(
                    "'{user_answer}' {phrase}.".format(
                        user_answer=user_answer,
                        phrase=settings.CASE_INCORRECT_WRONG,
                    )
                    + "{phrase} '{correct_answer}'.\n".format(
                        phrase=settings.CASE_INCORRECT_EXPECTED,
                        correct_answer=correct_answer,
                    )
                    + '{phrase}, {user_name}!'.format(
                        phrase=settings.CASE_INCORRECT_REPEAT,
                        user_name=user_name,
                    ),
                )
                break
        else:
            inform_user('{phrase}, {user_name}!'.format(
                phrase=settings.CONGRATULATIONS,
                user_name=user_name,
            ))
