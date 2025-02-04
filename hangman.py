# Hangman_game 
import random

Word_list = ["sudhanshu", "prausha","bob","camel",]

chosen_word = random.choice(Word_list)
print(chosen_word)


# todo 1 randomly choose a word form the word list  and assign it to a variable called chosen_word, then print it

placeholder = " "


for position in range(len(chosen_word)):
    placeholder = placeholder + "_"
print(placeholder)

game_over = False

correct_letters = []



while not game_over:


    guess = input("guess letter: ").lower()


    # todo 2  Ask  the user to guess a letter and assign the word to a variable called guess and make guess lower case
    guess = input("Guess a letter :").lower()


    # todo3 check if the letter the user guessed is one of the letters in the chosen_word. Print Right if it is and wrong if it is not.


    display = " "

    for letter in chosen_word:
        if letter == guess:
            print("Right")
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)


    if "_" not in display:
        game_over = True
        print("You won")





