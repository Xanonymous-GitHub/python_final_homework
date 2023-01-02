from secrets import choice
from typing import Tuple, List, Final, NoReturn, Sequence, TypeVar

T = TypeVar("T")

GAME_DIGITS_LENGTH: Final[int] = 4


class BullsCowsGame:
    __guess_history: List[str] = []

    def __init__(self):
        self.__ans = self.__gen_random_answer()

    # Generate a random answer.
    def __gen_random_answer(self) -> Tuple[str]:
        upper_bound: Final[int] = 10 ** GAME_DIGITS_LENGTH
        random_digits: Final[int] = self.__random_choose_from(range(0, upper_bound))
        formatted_digits: Final[str] = f"{random_digits:0{str(GAME_DIGITS_LENGTH)}d}"
        return tuple(c for c in formatted_digits)

    # Judge the given guess.
    def __judge_given_guess(self, guess: str) -> Tuple[int, int]:
        if len(guess) != len(self.__ans):
            raise ValueError

        correct_position: int = 0
        correct_digit: int = 0

        for i, c in enumerate(guess):
            if c == self.__ans[i]:
                correct_position += 1
            elif c in self.__ans:
                correct_digit += 1

        return correct_position, correct_digit

    # Show the result of the guess.
    def __show_guess_result(self, guess: str, correct_position: int, correct_digit: int) -> NoReturn:
        formatted_correct_position: Final[str] = f"{correct_position}A" if correct_position > 0 else ""
        formatted_correct_digit: Final[str] = f"{correct_digit}B" if correct_digit > 0 else ""
        formatted_judge_result: Final[str] = f"{formatted_correct_position}{formatted_correct_digit}" \
            if formatted_correct_position or formatted_correct_digit else "0"

        self.clear_cli()

        [print(h) for h in self.__guess_history]
        current_guess_result = f"{len(self.__guess_history) + 1:02d}: {guess} -> {formatted_judge_result}\n"
        print(current_guess_result)
        self.__guess_history.append(current_guess_result)

        if correct_position == GAME_DIGITS_LENGTH:
            print(f"Congratulation! You've got the number! It's {guess}!")
            raise SystemExit

    # Pick a random value from the given sequence.
    @staticmethod
    def __random_choose_from(seq: Sequence[T]) -> T:
        return choice(seq)

    # Receive the user's guess input.
    @staticmethod
    def __receive_user_guess_input() -> str:
        guess: Final[str] = input(f"Please input a {GAME_DIGITS_LENGTH}-digit number: ")
        if not guess.isdigit():
            print("You must enter only digits!")
            raise ValueError

        if len(guess) != GAME_DIGITS_LENGTH:
            print(f"You must enter exactly {GAME_DIGITS_LENGTH} digits!")
            raise ValueError

        return guess

    @staticmethod
    def clear_cli() -> NoReturn:
        print("\033[H\033[J")

    def start(self) -> NoReturn:
        print("Welcome to Bulls and Cows game!")
        print(f"The number is between {'0' * GAME_DIGITS_LENGTH} and {'9' * GAME_DIGITS_LENGTH}.")
        print("Let's start!\n")

        guess_number: int = 0

        while True:
            try:
                guess: str = self.__receive_user_guess_input()
                guess_number += 1
                correct_position, correct_digit = self.__judge_given_guess(guess)
                self.__show_guess_result(guess, correct_position, correct_digit)
            except ValueError:
                print("Please try again!\n")
            except KeyboardInterrupt:
                print("\nBye!")
                raise SystemExit


if __name__ == '__main__':
    if GAME_DIGITS_LENGTH < 1:
        print("The length of the game digits must be greater than 0!")
        raise ValueError

    game: Final[BullsCowsGame] = BullsCowsGame()
    game.start()
