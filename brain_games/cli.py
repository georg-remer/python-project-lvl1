"""User greeting module."""


import prompt


def welcome_user():
    """
    Promt user name and print greeting.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {name}!'.format(name=name)
