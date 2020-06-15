"""Module for input/output operations."""

import prompt


def ask_user():
    """
    Ask user to provider answer.

    Returns:
        str
    """
    return prompt.string('Your answer: ')


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
    name = prompt.string('May I have your name? ')
    inform_user('Hello, {name}!'.format(name=name))
    return name
