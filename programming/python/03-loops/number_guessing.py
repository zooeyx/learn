"""Number Guessing — a simple guessing game.

Exercises:
  1. Generate a random number 1-100
  2. Loop: ask for guesses, give "higher"/"lower" hints
  3. Count attempts and congratulate on correct guess
  4. Since we can't use input(), simulate with a list of guesses
"""

import random


def play_game(secret, guesses):
    """Play a guessing game with predetermined guesses.

    Args:
        secret: the number to guess
        guesses: list of guesses to try
    Returns:
        number of attempts, or -1 if not guessed
    """
    # TODO: Loop through guesses
    # TODO: For each guess, print "Too high", "Too low", or "Correct!"
    # TODO: Return the attempt number (1-indexed) on correct guess
    # TODO: Return -1 if no correct guess
    pass  # Remove when done


def main():
    random.seed(42)
    secret = random.randint(1, 100)
    print(f"(Secret number is {secret})")

    # TODO: Simulate a game with a list of guesses
    # Hint: guesses = [50, 25, 75, secret]
    # Hint: result = play_game(secret, guesses)

    pass  # Remove when done


if __name__ == "__main__":
    main()
