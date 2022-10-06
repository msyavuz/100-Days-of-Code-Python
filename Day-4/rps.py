from random import choice
from typing import Dict


def main():

    choices: Dict = {1: "Rock", 2: "Paper", 3: "Scissors"}

    ascii_art: Dict = {1: """
                                _______
                            ---'   ____)
                                (_____)
                                (_____)
                                (____)
                            ---.__(___)
                            """, 2: """
                                _______
                            ---'    ____)____
                                    ______)
                                    _______)
                                    _______)
                            ---.__________)
                            """, 3: """
                                _______
                            ---'   ____)____
                                    ______)
                                __________)
                                (____)
                            ---.__(___)
                            """}

    user_choice: int = int(input(
        "Welcome to Rock, Paper, Scissors. Choose! (1 for Rock, 2 for Paper, 3 for Scissors) \n"))
    computer_choice: int = int(choice(list(choices.keys())))

    result: str = "Draw"

    if user_choice == 1 and computer_choice == 3:
        result = "You win!"

    elif user_choice == 1 and computer_choice == 2:
        result = "You lose!"

    elif user_choice == 2 and computer_choice == 1:
        result = "You win!"

    elif user_choice == 2 and computer_choice == 3:
        result = "You lose!"

    elif user_choice == 3 and computer_choice == 2:
        result = "You win!"

    elif user_choice == 3 and computer_choice == 1:
        result = "You lose!"

    print(f"You chose: {choices[user_choice]}")
    print(ascii_art[user_choice])
    print(f"Computer chose: {choices[computer_choice]}")
    print(ascii_art[computer_choice])
    print(result)


if __name__ == "__main__":
    main()
