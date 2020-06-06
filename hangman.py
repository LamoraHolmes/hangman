import random
import os
import sys
from drawing import hangman_picture

attemps = 0
word = ""
letter = ""
guessed_letter_list = []
guesses = set()

def generate_wordlist():
    with open(os.path.join(sys.path[0], 'wordlist.txt'), "r") as f:
            
            wordlist = [line.rstrip() for line in f]
            f.close()
            return wordlist

def random_word(wordlist):
    random_number = random.randint(0,len(wordlist)-1)

    return wordlist[random_number]


def turn():
    
    global attemps, word, letter, guessed_letter_list, guesses

    result = evaluate()
    
    hangman_picture(attemps)
    print(f"{guessed_letter_list}               #characters you alreasy guessed {guesses}")
    print("")

    if result:
        print(f"Your letter ({letter}) was right")
    else:
        print(f"Your letter ({letter}) was wrong")

    if attemps == 6:
        return
    elif guessed_letter_list == list(word):
        return
    
    
    letter = input("Guess another letter: ")
    
    while letter in guesses:
        print("You already guesses this letter.")
        print("")
        letter = input("Please guess another letter: ") 
    
    guesses.add(letter)

    print("")


def evaluate():

    global word, attemps, guessed_letter_list, letter

    if letter in list(word):
        index = [index for index,value in enumerate(word) if value == letter]
        
        for i in index:
            guessed_letter_list[i] = letter

        return True

    else:
        attemps += 1
        return False
    



def welcome_message():

    global word, letter, guessed_letter_list, attemps, guesses

    print("")
    print("##########################")    
    print("### Welcome to Hangman ###")
    print("##########################")
    print("")
    start_game = input("Do you want to play a game with me? y/n: ")

    if start_game:
        answer = "y"
        while answer == "y":            

                wordlist = generate_wordlist()
                word = random_word(wordlist)

                guessed_letter_list = ["_" for i in range(0,len(word))]

                print("")
                print(f"Your word is {len(word)} Characters long.")
                letter = input("Guess a letter: ")
                guesses.add(letter)
                print("")

                while attemps < 6 and guessed_letter_list != list(word):
                    turn()

                if attemps > 5:
                    print("You lost the game")
                    print("")
                    print(f"The correct answer would've been: {word}")
                    print("")
                    answer = input("Do you want to start another game? y/n: ")
                elif guessed_letter_list == list(word):
                    print(f"You are right. The correct word was: {word}")
                    print("")
                    answer = input("Do you want to start another game? y/n: ")

    return


welcome_message()