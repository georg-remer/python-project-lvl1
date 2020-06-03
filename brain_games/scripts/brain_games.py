"""Main module."""

from brain_games.cli import welcome_user

INTRO = 'Welcome to the Brain Games!'


def get_intro():
    """Return intro.

    Returns:
        str
    """
    return INTRO


def main():
    """Print intro and welcome user."""
    print('{intro}\n'.format(intro=get_intro()))

    greeting = welcome_user()[0]
    print(greeting)


if __name__ == '__main__':
    main()
