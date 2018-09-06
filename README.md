# spaceman
Hangman but renamed to Spaceman. Pretty dope. 

Let's start with some PSEUDOCODE!!

Needs: 
list holding guessed letters
string holding the secret word, replaceable '_'
ability to create new string with the guessed letters replaced
counter for the number of guesses

Game Flow: 
"Welcome to the game of Spaceman!"
show the string holding the secret word (in underscores)
prompts user to enter a letter
checks if the input is a letter
checks if the input matches with a letter from the word, counter ++
  -if does match, change the string holding the secret word, show the secret word with underscores
  -if does not match, do nothing, show the secret word with underscores
loops until word is guessed or 7 guesses are made  
show the whole secret word
