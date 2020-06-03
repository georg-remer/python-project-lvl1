"""User greeting module."""


import prompt


def welcome_user():
    """
    Promt user name.

    Returns tuple consisting of greeting itself and name of the user

    Returns:
        (str, str)
    """
    name = prompt.string('May I have your name? ')
    return ('Hello, {name}!'.format(name=name), name)


def ask_for_answer():
    """
    Ask user to provider answer.

    Returns:
        str
    """
    return prompt.string('Your answer: ')
