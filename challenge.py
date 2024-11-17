import random

#print hangman function (will be the multiple stages of the game)
def print_hangman(a, numb_of_letters):
    if a == 0:
        print("     +---+\n     |   |\n         |\n         |\n         |\n         |\n     =========")
        print(f"Welcome to hangman! You have 6 tries to guess the correct word. This word has {numb_of_letters} letters in it.")
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
    #create win condition and print words "you win! the word was __. it took you __ guesses."

#function that takes a random input from word bank and splits it into an array for each letter then outputs a list with a respective number of _ for the length
def word_pick(wordlist):
    word = random.choice(wordlist)
    list_word = list(word)

    return list_word, word

#function that updates the spaces displayed with correct letters
def guess_input(array, counter, answer, wrong_guesses, correct_counter, incorrect_counter):
    original_list = array.copy()
    a = -1
    guess = input("Please guess a letter.\n")
    capital_guess = guess.upper()
    for letter in answer:
        a += 1
        if capital_guess == letter:
            array[a] = capital_guess
            correct_counter += 1
    if original_list == array:
        counter += 1
        wrong_guesses.append(guess)
        incorrect_counter += 1
    if array == answer:
        counter = 7

    return counter, correct_counter, incorrect_counter

#function that displays the number of guesses and how many have been correct & incorrect

#create a try again? function
    #if yes then restart game
    #if no then end the program

def game_start():
    play = 1
    while play == 1:
        #list of possible words
        possible_words = ["COMPUTER", "PYTHON", "BYU", "HANGMAN", "INCORRECT", "CORRECT", "INFORMATION", "PRACTICE", "CHALLENGE", "WINNER"]
        #the variable for the word
        word_to_guess, word = word_pick(possible_words)
        counter = 0
        interface_word = []
        letter_count = 0
        incorrect_guesses = []
        guess_counter = 0
        correct_number = 0
        incorrect_number = 0
        #creating the appropriate length for the word
        for letter in word_to_guess:
            interface_word.append("_")
            #counts the letters for the beginning statement
            letter_count += 1
        #interates through each round until win or lose
        while counter < 6:
            print_hangman(counter, letter_count)
            final_string = ""
            for item in interface_word:
                final_string += item
            print(final_string)
            wrong_string = ""
            for item in incorrect_guesses:
                wrong_string += item
            print(f'Letters guessed: {wrong_string}')
            print(f'Number of guesses: {guess_counter} | Number of correct: {correct_number} | Number of incorrect: {incorrect_number}')
            counter, correct_number, incorrect_number = guess_input(interface_word, counter, word_to_guess, incorrect_guesses, correct_number, incorrect_number)
            guess_counter += 1
        if counter == 7:
            print(f'You won! The word was {word}. It took you {guess_counter} guesses.')
        else:
            print_hangman(counter, letter_count)
            print(f'GAME OVER! The word was {word}.')
        again = input("Would you like to play again? Y or N \n")
        again_final = again.upper()
        if again_final == "N":
            print("Bye, bye!")
            play = 2

#main function here
game_start()