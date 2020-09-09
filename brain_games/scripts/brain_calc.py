"""Calculator game script."""

from brain_games.games import brain_calc
from brain_games.games.engine import play


def main():
    """Play the game: Calculator."""
    play(brain_calc)


if __name__ == '__main__':
    main()
