import random

# REMEMBER strings in Python are IMMUTABLE!!
# TASKS: check for input type (control-space and control-d)

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_guess_valid(the_guess):
    valid_guesses = list("abcdefghijklmnopqrstuvwxyz")
    if the_guess in valid_guesses:
        return True
    else:
        return False

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE...
    #example: is_word_guessed("cat", "tac"), returns True
    #example: is_word_guessed("cat", "ct"), returns False

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

# is_word_guessed("cat", "cat")


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    # example: get_guessed_word("cat", "tac") returns cat
    # example: get_guessed_word("cat", ta") returns _at
    # _ _ _ , _ _ t , _ a t
    num_underscores = len(secret_word)
    guess_so_far = ""
    for underscores in range(num_underscores):
        guess_so_far = guess_so_far + "_"

    updated_guess_so_far = guess_so_far
    for letter in letters_guessed:
        found_index = secret_word.find(letter)
        # is the letter in the secret_word? if so, replace the underscore with that letter (count by index?)
        # replaces the first instance of the letter found, but what about following instances??
        while secret_word[found_index:].find(letter) != -1:
            updated_guess_so_far = updated_guess_so_far[:found_index] + letter + updated_guess_so_far[found_index+1:]
            if found_index == len(secret_word) - 1 or secret_word[found_index + 1:].find(letter) == -1:
                break
            found_index = (found_index + 1) + secret_word[found_index + 1:].find(letter)
            print ("found_index = " + str(found_index))

    print("updated_guess_so_far = " + updated_guess_so_far)
    return updated_guess_so_far

def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    letters_not_guessed = "abcdefghijklmnopqrstuvwxyz"

    for letter in letters_guessed:
        letters_not_guessed = letters_not_guessed.replace(letter, "")

    print(letters_not_guessed)
    return letters_not_guessed

def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Spaceman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Spaceman! The word that you will be guessing in 7 turns contains %d letters" %(len(secret_word)))
    print("Please guess just one letter per round.")

    total_letters_guessed = ""
    total_guesses_left = 7

    while is_word_guessed(secret_word, total_letters_guessed) != True or total_guesses_left > 0:
        try:
            guess = input("Please guess one letter: ")
            if is_guess_valid(guess):
                total_letters_guessed = total_letters_guessed + guess
                # print("total_guesses_left = " + str(total_guesses_left))
                if secret_word.find(guess) != -1:
                    print("Yay! Your letter was in the word and the word now looks like this:")
                    get_guessed_word(secret_word, total_letters_guessed)
                    print("You also now have the following letters left to use:")
                    get_available_letters(total_letters_guessed)
                    print("You have a total number of %d guesses left" %(total_guesses_left))
                    if total_guesses_left == 0:
                        break
                else:
                    total_guesses_left = total_guesses_left - 1
                    print("Try again! You have %d guesses left!" %(total_guesses_left))
                    if total_guesses_left == 0:
                        break
            else:
                print("Try entering a lowercase letter from the alphabet!")
        except EOFError:
            print("Ugh. Please don't try to break this piece of code.")

    if is_word_guessed(secret_word, total_letters_guessed):
        print("Congratulations! You have guessed the word before Spaceman blasted off into space!")
    else:
        print(f"I'm sorry, you did not guess the word secret word: {secret_word}. Spaceman will now be blasted off into space! Awww.")



#
secret_word = load_word()
spaceman(load_word())
