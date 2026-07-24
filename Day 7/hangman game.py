import random

word_list=["cake", "melons", "jupiter"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
gameover = False
correctLetters = []
while not gameover:
    user_guess = input("enter your guess").lower()
    display=""
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correctLetters.append(user_guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        gameover = True
        print("you win")

