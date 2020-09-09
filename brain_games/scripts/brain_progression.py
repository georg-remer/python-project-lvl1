"""Brain Progression game script."""

from brain_games.games import brain_progression
from brain_games.games.engine import play


def main():
    """Play the game: Brain Progression."""
    play(brain_progression)


if __name__ == '__main__':
    main()
