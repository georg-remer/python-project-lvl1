"""Main module."""


from brain_games.cli import welcome_user


def main():
    """Greet user."""
    print('Welcome to the Brain Games!\n')
    print(welcome_user())


if __name__ == '__main__':
    main()
