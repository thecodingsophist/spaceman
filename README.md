# UFO: THE GAME

This game was created for the Codeacademy 2019 Summer internship.

Play it to see what it's about! Run "python3 UFO_game.py" in your terminal to play the game!

PLAY HINT: In the very beginning of the game, there will be many possible words that populate the possible_words_list, and will most likely fill up most of the screen. At the bottom of the screen, there will be a prompt that asks to guess a letter. I suggest starting with a vowel ('a - e - i - o - u') to eliminate a good number of the possible words in the possible_words_list and to see the entirety of the different things that are going on in the game. Otherwise, scroll up to see everything that is going on in the game.

TESTS: Run "python3 UFO_unit_tests.py" in your terminal to make sure all functions are working correctly and modularly. Note: There is one test (get_guessed_word) that didn't pass and needs a bit of tweaking.


ENJOY!

FUTURE IMPROVEMENTS: Allow user to guess the entire word at any point of the game at the expense of one guess.

-----------------------------------------

Let's start with some PSEUDOCODE!!

Needs:
list holding guessed letters, displays the letters
string holding the secret word, replaceable _
ability to create new string with the guessed letters replaced
counter for the number of guesses

Game Flow:

"Welcome to the game of UFO! Danger is imminent and you must save yourself from being abducted by the UFOs by trying to correctly guess the word as represented by the underscores below! You have six letter guesses, should you guess correctly, you will be safe! If not.. you will be abducted into the unknown world! We will help you by revealing the words that it could be based on your letter guesses. Are you ready?"

show the string holding the secret word (in underscores)

prompts user to enter a letter

checks if the input is a letter

checks if the input matches with a letter from the word, counter ++

  -if does match, change the string holding the secret word, show the secret word with underscores
  -if does not match, do nothing, show the secret word with underscores

add suggestions of possible words from dictionary


loops until word is guessed or 6 guesses are made

show the whole secret word
