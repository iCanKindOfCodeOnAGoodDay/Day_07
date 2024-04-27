"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 7
    April 26 2024

    ------
    Description:    Hangman
    ------
    
    ------
    Inputs:         Words are hardcoded, User input
    ------
    
    ------
    Outputs:        Hangman Game
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
    
    hangman_words = [ "mystery", "quartz", "jazz", "buzz", "fuzzy", "vortex", "jackpot", "zigzag", "quiz", "oxygen", "ivy", "strength", "rhythm", "lynx", "pixel", "zombie", "kayak", "gazebo", "equip", "galaxy", "walker", "whiskey", "jinx", "jukebox", "kiosk", "haiku", "fluff", "jiffy", "haphazard", "embezzle", "bikini", "blizzard", "espionage", "flapjack", "gnarly", "humble", "ivory", "jump", "knight", "light", "mango", "nugget", "ostrich", "penguin", "quiver", "river", "sphinx", "tornado", "umbrella", "vampire" ]

    R = random.randint(0, len(hangman_words))
    
    R_word = hangman_words[R]
    
    word_length = len(R_word)
    
    word_with_blanks = list(initalize_word(R_word))
    
    print('\n\n')
    
    print(word_with_blanks, end='\n\n\n\n\n')
    
    guesses = 6
    
    print(draw_gallows(0))
    
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

    word = ''
    for char in R_word:
        word += '_'
        
    return word 
        
    
    
if __name__ == '__main__':
    main()