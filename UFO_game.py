import random
from ufo import *

def load_word():
   f = open('nouns.txt', 'r')
   words_list = f.readlines()
   f.close()

   # words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_guess_valid(the_guess):
    valid_guesses = list("abcdefghijklmnopqrstuvwxyz")
    if the_guess in valid_guesses:
        return True
    else:
        return False

def is_guess_original(the_guess, letters_guessed):
    if the_guess in letters_guessed:
        print("Oh no! You've already guessed that letter. Try again")
        return False
    else:
        return True

def is_word_guessed(secret_word, letters_guessed):
    new_secret_word = secret_word

    for letter in letters_guessed:
        new_secret_word = secret_word.replace(letter, "")
        secret_word = new_secret_word
    if new_secret_word == "":
        # print("t")
        return True
    else:
        # print("f")
        return False

def get_guessed_word(secret_word, letters_guessed):
    num_underscores = len(secret_word)
    guess_so_far = ""
    for underscores in range(num_underscores):
        guess_so_far = guess_so_far + "_"

    updated_guess_so_far = guess_so_far
    for letter in letters_guessed:
        found_index = secret_word.find(letter)
        # is the letter in the secret_word? if so, replace the underscore with that letter (count by index?)
        while secret_word[found_index:].find(letter) != -1:
            updated_guess_so_far = updated_guess_so_far[:found_index] + letter + updated_guess_so_far[found_index+1:]
            if found_index == len(secret_word) - 1 or secret_word[found_index + 1:].find(letter) == -1:
                break
            found_index = (found_index + 1) + secret_word[found_index + 1:].find(letter)
            # print ("found_index = " + str(found_index))

    print("Your guess so far: " + updated_guess_so_far)
    return updated_guess_so_far

def get_available_letters(letters_guessed):

    letters_not_guessed = "abcdefghijklmnopqrstuvwxyz"

    for letter in letters_guessed:
        letters_not_guessed = letters_not_guessed.replace(letter, "")

    print(letters_not_guessed)
    return letters_not_guessed

def UFO_game(secret_word):

    game_running = False
    total_letters_guessed = ""
    total_guesses_left = 6
    letters_guessed = ""

    usr_input = input("Welcome to the game of UFO! Danger is imminent and you must save yourself from being abducted by the UFOs by trying to correctly guess the word as represented by the underscores below! You have six letter guesses, should you guess correctly, you will be safe! If not.. you will be abducted into the unknown world! We will help you by revealing the words that it could be based on your letter guesses. Are you ready? y/exit")
    if usr_input == "y":
        game_running = True
    else:
        exit()

    while game_running and (is_word_guessed(secret_word, total_letters_guessed) != True or total_guesses_left > 0):
        try:
            get_guessed_word(secret_word, letters_guessed)
            guess = input("Please guess one letter: ")
            # print("guess=" + guess)
            if is_guess_valid(guess) and is_guess_original(guess, letters_guessed):
                letters_guessed += guess
                total_letters_guessed = total_letters_guessed + guess
                # print("total_guesses_left = " + str(total_guesses_left))
                if secret_word.find(guess) != -1:
                    print("Yay! Your letter was in the word and the word now looks like this:")
                    get_guessed_word(secret_word, total_letters_guessed)
                    # print("You also now have the following letters left to use:")
                    # get_available_letters(total_letters_guessed)
                    print("You have a total number of %d guesses left" %(total_guesses_left))
                    print("Be careful though! You are now this far away from getting abducted!")
                    print(x[6-total_guesses_left])
                    if total_guesses_left == 0:
                        break
                else:
                    total_guesses_left = total_guesses_left - 1
                    print("Oh no! You are getting closer to the alien spaceship! Try again! You have %d guesses left!" %(total_guesses_left))
                    get_guessed_word(secret_word, letters_guessed)
                    print(x[6-total_guesses_left])
                    if total_guesses_left == 0:
                        break
            else:
                print("Try entering another lowercase letter from the alphabet!")

        except EOFError:
            print("Ugh. Please don't try to break this piece of code.")

    if is_word_guessed(secret_word, total_letters_guessed):
        print("Congratulations! You have guessed the word before you were abducted by the aliens!")
    else:
        print(f"I'm sorry, you did not guess the word secret word: {secret_word}. You have now been abducted into outerspace!")



# START GAME
secret_word = load_word()
UFO_game(load_word())
