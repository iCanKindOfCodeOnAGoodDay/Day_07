"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 7
    April 26 2024

    ------
    Description:    Hangman - Console input/ output game
    ------
    
    ------
    Inputs:         Console input
    ------
    
    ------
    Outputs:        Console output
    ------
    
    ------
    Dependencies:   Random
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import random


def main():
    """
    Description - Runs hangman
    ------
    
    Inputs - Gameplay requires user input in console
    ------

    Outputs - Gameplay
    ------
        
    """
    
    hangman_words = [ "mystery", "quartz", "jazz", "buzz", "fuzzy", "vortex", "jackpot", "zigzag", "quiz", "oxygen", "ivy", "strength", "rhythm", "lynx", "pixel", "zombie", "kayak", "gazebo", "equip", "galaxy", "walker", "whiskey", "jinx", "jukebox", "kiosk", "haiku", "fluff", "jiffy", "haphazard", "embezzle", "bikini", "blizzard", "espionage", "flapjack", "gnarly", "humble", "ivory", "jump", "knight", "light", "mango", "nugget", "ostrich", "penguin", "quiver", "river", "sphinx", "tornado", "umbrella", "vampire" ]

    R_word = pick_word()
    
    word_length = len(R_word)
    
    word_with_blanks = initalize_word(R_word)
    
    print('\n\n')
    
    print(word_with_blanks, end='\n\n\n\n\n')
    
    print(draw_gallows(0))
    
    run_game(R_word, word_with_blanks)
    

def pick_word( hangman_words ):
    """
    Description - Returns a random word from the list
    ------
    
    Inputs - Words are hardcoded in main func for now
    ------

    Outputs - One of the words
    ------
        
    """

    R = random.randint(0, len(hangman_words))
    
    R_word = hangman_words[R]
    
    return R_word


def run_game(R_word, word_with_blanks):
    """
    Description - Runs hangman, console game with user input and game in console
    ------
    
    Inputs 
    ------
        
    User input in console
    word with blanks is the random word as a list with characters hidden, revealed as user guesses correctly
    
    ------

    Outputs - Gameplay in console
    ------
        
    """
    
    guesses = 6
    guesses_used = 0
 
    while guesses >= 0:
        correct_guess = False
        g = input('\n\n\nGuess a letter: ')
        for i in range(len(R_word)):
            if R_word[i] == g:
                word_with_blanks[i] = g
                correct_guess = True
            else:
                if correct_guess == False: # so we don't overrite previous correct guesses
                    correct_guess = False
            
        if correct_guess == False:
    
            print(word_with_blanks)
            guesses -=1
            guesses_used +=1
            print(draw_gallows( guesses_used ))

            if guesses == 0:
                print('Game over')
                break
            print(f'\nWhoops! You\'ve got {str(guesses)} left!\n\n')
            #print(draw_gallows( guesses_used ))
        
        else:
            print(f'NICE!\n\n\n{word_with_blanks}')
            print(draw_gallows( guesses_used ))
            
    print('\n\n\ngame over!')
    print(draw_gallows( guesses_used ))

                     
def draw_gallows( guesses_used ):
    """
    Description - Library for ASCII art messages in console
    ------
    
    Inputs - Guesses used can't go over index count or there will be error
    ------

    Outputs - Text for the console based on index (guesses_used)
    ------
        
    """
    
    hangman_steps = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]
   
    gallows = hangman_steps[guesses_used]
    return gallows

    
def initalize_word( R_word ):
    """
    Description - starting point for the hidden word that is displayed for users to guess letters belong to
    ------
    
    Inputs - Loops through the random word characters
    ------
    
    Outputs - Outputs an underscore for each of the letters
    ------
        
    """
    
    word = []
    for char in R_word:
        word.append('_')
        
    return word 
        

# run
if __name__ == '__main__':
    main()
