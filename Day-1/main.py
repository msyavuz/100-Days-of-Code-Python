def main() -> None:
    print("Welcome to the Band Name Generator.\n")
    city_name: str = input("What's the name of the city you grew up in?\n")
    pet_name: str = input("What's your pet's name?\n")
    possible_name: str = f"{city_name} {pet_name}"
    print(f"Your band name could be {possible_name}")


if __name__ == "__main__":
    main()
