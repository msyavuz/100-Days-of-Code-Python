from typing import List
from random import shuffle, choice
import string


def main():

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to password generator. \n")
    nr_letters: int = int(input(
        "How many letters would you like in your password?\n"))
    nr_numbers: int = int(input(
        "How many digits would you like in your password?\n"))
    nr_symbols: int = int(input(
        "How many symbols would you like in your password?\n"))

    result_list: List[str] = []

    for i in range(nr_letters):
        result_list.append(choice(string.ascii_letters))
    for i in range(nr_numbers):
        result_list.append(choice(string.digits))
    for i in range(nr_symbols):
        result_list.append(choice(symbols))

    shuffle(result_list)

    print(f"Your password is: {''.join(result_list)}")


if __name__ == "__main__":
    main()
