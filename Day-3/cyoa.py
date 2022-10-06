def main():
    ascii_art: str = r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************'''

    print(ascii_art+"\n")
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice_1: str = input(
        "You are at a crossroads. Where do you want to go? (left, right) ").lower()

    if choice_1 == "left":

        choice_2 = input(
            "You came across a lake with an island in the centre. Wait for a boat or swim across? (wait, swim) ").lower()

        if choice_2 == "wait":
            choice_3 = input(
                "You arrive at the island unharmed. There is a house with 3 doors; red, yellow, blue. Which will you choose? ").lower()

            if choice_3 == "blue":
                print("Congrats! You got to the treasure room. \nYou Win!")
            else:
                print("It was a room full of fire. \nGame Over")

        else:
            print("You got attacked by an alligator. \nGame Over")
            exit()
    else:
        print("You fell into a hole. \nGame Over")
        exit()


if __name__ == "__main__":
    main()
