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
import prompt

from brain_games import settings


def ask_user():
    """
    Ask user to provider answer.

    Returns:
        str
    """
    return prompt.string(
        '{prompt}: '.format(prompt=settings.PROMPT_FOR_ANSWER),
    )


def inform_user(information):
    """Print information to user.

    This is the only place that prints any information to user.
    No other module uses 'print'

    Args:
        information: information to be printed out to user
    """
    print(information)


def welcome_user():
    """
    Promt user name.

    Returns name of the user

    Returns:
        str
    """
    name = prompt.string(
        '{prompt}: '.format(prompt=settings.PROMPT_FOR_NAME),
    )
    inform_user('{greeting}, {name}!\n'.format(
        greeting=settings.GREETING, name=name,
    ))
    return name


def play(game):
    """Game flow.

    Plays the game if specified, or just greets user

    Args:
        game: Game module
    """
    # Print intro
    inform_user(settings.INTRO)

    # Get game setup and print it's description
    inform_user('{description}\n'.format(description=game.GAME_DESCRIPTION))

    # Welcome user and get user name
    user_name = welcome_user()

    # Get question and correct answer, play the game
    for _ in range(settings.NUMBER_OF_ROUNDS):
        (question, correct_answer) = game.get_question_with_answer()
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
