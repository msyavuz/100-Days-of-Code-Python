from random import choice
banner_text = r""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/          """
hanged_man_0 = r"""

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___

"""
hanged_man_5 = r"""

      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___

"""
hanged_man_4 = r"""

      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___

"""
hanged_man_3 = r"""

      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___

"""
hanged_man_2 = r"""

      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___

"""
hanged_man_1 = r"""

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___

"""

stages = [hanged_man_0, hanged_man_1,hanged_man_2,hanged_man_3, hanged_man_4, hanged_man_5]

with open("Day-7/words.txt", "r", encoding="utf-8") as f:
    chosen_word = choice(f.readlines())


curr_charlist = ["_" for i in chosen_word[1:]]

curr_word = "".join(curr_charlist)

remaining_guesses = 5

print(banner_text)
print(hanged_man_5)
print(chosen_word)

print("".join(curr_charlist))

while remaining_guesses>0:

    print("".join(curr_charlist)==chosen_word)
    if "".join(curr_charlist)==chosen_word:
        break
    guess = input("Enter a character \n")[0]
    if guess in chosen_word:
        for index, char in enumerate(chosen_word):
            if char == guess:
                curr_charlist[index] = guess
                curr_word = "".join(curr_charlist)

        print(stages[remaining_guesses])
        print(curr_word)
    else:
        remaining_guesses-=1
        print(stages[remaining_guesses])
        print(curr_word)

if remaining_guesses==0:
    print("You lost!")

elif remaining_guesses>=0:
    print("You won!")

print(f"Word was: {chosen_word}")
