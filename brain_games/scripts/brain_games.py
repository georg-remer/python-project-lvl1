"""Main module."""

from brain_games.games.engine import play_game


def main():
    """Play the game.

    No game is specified, so it greets the user only.
    """
    play_game()


if __name__ == '__main__':
    main()
