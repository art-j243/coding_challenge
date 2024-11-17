## Hangman Coding Challenge in Python
### Arthur Carter

This was written for a computer programmer job application at BYU. Notes regarding my process are commented into my python file and a snapshot of the beginning of my process is copied over into the readme file. No external libraries were used. The program succesfully runs in the terminal with all the requirements completed along with the "exta credit."

This code took me a total of 2 hours and 56 minutes.

Thank you for your consideration!





## Snapshot of beginning process

import random

#functions

#print hangman function (will be the multiple stages of the game)
def print_hangman(a):
    if a == 0:
        print("     +---+\n     |   |\n         |\n         |\n         |\n         |\n     =========")
        print("Welcome to hangman! You have 6 tries to guess the correct word.")
    if a == 1:
        print("     +---+\n     |   |\n     O   |\n         |\n         |\n         |\n     =========")
    if a == 2:
        print("     +---+\n     |   |\n     O   |\n     |   |\n         |\n         |\n     =========")
    if a == 3:
        print("     +---+\n     |   |\n     O   |\n    /|   |\n         |\n         |\n     =========")
    if a == 4:
        print("     +---+\n     |   |\n     O   |\n    /|\\  |\n         |\n         |\n     =========")
    if a == 5:
        print("     +---+\n     |   |\n     O   |\n    /|\\  |\n    /    |\n         |\n     =========")
    if a == 6:
        print("     +---+\n     |   |\n     O   |\n    /|\\  |\n    / \\  |\n         |\n     =========")

    #need one for each limb and one for the beginning of the game

    #create win condition and print words "you win! the word was __. it took you __ guesses."

#function that takes a random input from word bank and splits it into an array for each letter then outputs a list with a respective number of _ for the length
    #add a line that prints the number of letters

#function that updates the spaces displayed with correct letters
    #also displays a list of incorrect previous guesses

#function that displays the number of guesses and how many have been correct & incorrect

#create a try again? function
    #if yes then restart game
    #if no then end the program

#function that starts the game when called
def game_start():
    #word bank
    word_bank = ["BYU"]
    #set variables like counter and such
    counter = 0
    #start while loop for game. loop will go until the word is guess or user loses
    while counter < 6:
        #print hangman function is called to begin the game and 
        print_hangman(counter)
        






#main function here