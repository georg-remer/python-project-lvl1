"""GCD game script."""

from brain_games.games import brain_gcd
from brain_games.games.engine import play


def main():
    """Play the game: GCD."""
    play(brain_gcd)


if __name__ == '__main__':
    main()
