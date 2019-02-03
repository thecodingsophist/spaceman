# UFO: THE GAME

This game was created for the Codeacademy 2019 Summer internship.

Play it to see what it's about! Run "python3 UFO_game.py" in your terminal to play the game! 

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

loops until word is guessed or 6 guesses are made

show the whole secret word
