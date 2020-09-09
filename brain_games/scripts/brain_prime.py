"""Prime number game script."""

from brain_games.games import brain_prime
from brain_games.games.engine import play


def main():
    """Play the game: Prime Number."""
    play(brain_prime)


if __name__ == '__main__':
    main()
