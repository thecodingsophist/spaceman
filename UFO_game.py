import random
import sys
from ufo import *

# this loads the word from the dictionary
def load_word():
   f = open('nouns.txt', 'r')
   words_list = f.readlines()
   f.close()

   # words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

#  this sees if the guessed letter is an actual letter
def is_guess_valid(the_guess):
    valid_guesses = list("abcdefghijklmnopqrstuvwxyz")
    print(valid_guesses)
    if the_guess in valid_guesses:
        return True
    else:
        return False

# this sees if the guess is original
def is_guess_original(the_guess, letters_guessed):
    if the_guess in letters_guessed:
        print("Oh no! You've already guessed that letter. Try again")
        return False
    else:
        return True

def is_word_guessed(secret_word, letters_guessed):
    new_secret_word = secret_word
    print("is_word_guessed is run")
    for letter in letters_guessed:
        new_secret_word = secret_word.replace(letter, "")
        secret_word = new_secret_word
        #print("new_secret_word" + str(len(new_secret_word)))
    #for some reason, the new secret word has to have 1 letter, not sure what the letter is
    if len(new_secret_word) <= 1:
        print("is word guessed is true")
        return True
    else:
        print("is word guessed is false")
        return False

def get_guessed_word(secret_word, letters_guessed):
    num_underscores = len(secret_word)
    guess_so_far = ""
    # Is range upperbound inclusive or exclusive?
    for underscores in range(num_underscores-1):
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

    print(updated_guess_so_far)
    return updated_guess_so_far

def word_reader(updated_guess_so_far):
    index = 0
    dictionary_of_letters = {}
    for letter in updated_guess_so_far:
        if letter != "_":
            dictionary_of_letters[index] = letter
        index += 1
    return dictionary_of_letters

# here dicitonary_of_letters is represented by secret_word_bits, which is ultimately a dicitonary

def word_searcher(secret_word_bits, excluded_letters):
    f = open('nouns.txt', 'r')
    words_list = f.readlines()
    f.close()
    possible_words_list = []
    for word in words_list:
        if len(secret_word_bits) != len(word.strip('\n')):
           continue
        else:
           #use word_reader to convert the word in words_list into a dictionary that can be compared with a dicitonary from the updated_guess_so_far
           dictionary_of_letters_in_words_list = word_reader(word)
           superset = dictionary_of_letters_in_words_list
           dictionary_of_letters_in_secret_word_bits = word_reader(secret_word_bits)
           subset = dictionary_of_letters_in_secret_word_bits
           if all(item in superset.items() for item in subset.items()):
               possible_words_list.append(word.strip('\n'))
    # print(possible_words_list)
    filtered_list = []
    for word in possible_words_list:
        letter_found = False
        # print("word high level: " + word)
        for letter in excluded_letters:
            # print("letter high level: " + letter)
            if letter in word:
                letter_found = True
                # print("word: " + word)
                # possible_words_list.remove(word)
                break
        if letter_found == False:
            filtered_list.append(word)

    print(filtered_list)
    return filtered_list

def get_available_letters(letters_guessed):

    letters_not_guessed = "abcdefghijklmnopqrstuvwxyz"

    for letter in letters_guessed:
        letters_not_guessed = letters_not_guessed.replace(letter, "")

    print(letters_not_guessed)
    return letters_not_guessed

def noUnderscore(guessed_word):
    count= len(guessed_word)
    for c in guessed_word:
        if c != "_": #this needs to be the correct character
            count-=1
    if count == 0:
        return True
    else:
        return False

def UFO_game(secret_word):

    game_running = False
    total_letters_guessed = ""
    excluded_letters = ""
    total_guesses_left = 6
    letters_guessed = ""

    usr_input = input("Welcome to the game of UFO! Danger is imminent and you must save yourself from being abducted by the UFOs by trying to correctly guess the word as represented by the underscores below! You have six letter guesses, should you guess correctly, you will be safe! If not.. you will be abducted into the unknown world! We will help you by revealing the words that it could be based on your letter guesses. Are you ready? y/exit")
    if usr_input == "y":
        game_running = True
    else:
        exit()


    guessed_word = ""
    while game_running and is_word_guessed(secret_word, letters_guessed) == False and total_guesses_left > 0:
    # while game_running and noUnderscore(guessed_word) == False and total_guesses_left > 0:
        try:
            sys.stdout.flush()
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print("Your guessed word looks like this so far: ")
            print(guessed_word)
            print("Your guessed word is one of the following words:")
            word_searcher(guessed_word, excluded_letters)
            guess = input("Please guess one letter: ")
            # print("guess=" + guess)
            if is_guess_valid(guess) and is_guess_original(guess, letters_guessed):
                letters_guessed += guess
                total_letters_guessed = total_letters_guessed + guess
                # print("total_guesses_left = " + str(total_guesses_left))
                if secret_word.find(guess) != -1:
                    print("Yay! Your letter was in the word and the word now looks like this:")
                    get_guessed_word(secret_word, total_letters_guessed)
                    print("You also now have the following letters left to use:")
                    get_available_letters(total_letters_guessed)
                    letters_guessed += guess
                    #print("letters_guessed" + letters_guessed)
                    print("You have a total number of %d guesses left" %(total_guesses_left))
                    print("Be careful though! You are now this far away from getting abducted!")
                    print(x[6-total_guesses_left])
                    if total_guesses_left == 0:
                        break
                else:
                    total_guesses_left = total_guesses_left - 1
                    excluded_letters = excluded_letters + guess
                    print("EXCLUDED_LETTERS:" + excluded_letters )
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
if __name__ == '__main__':
    UFO_game(load_word())
