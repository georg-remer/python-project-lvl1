"""Module for input/output operations."""

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
