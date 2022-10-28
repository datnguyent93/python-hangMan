import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)    #ltters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have guessed these letters: ', ' '.join(used_letters))
        
        #what guess correctly so far
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ' , ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word, silly')
                print(f'Your lives have {lives} live(s) left')
        
        elif user_letter in used_letters:
            print('You have used that char. Try different one')
        
        else:
            print('Invalid char. Try different one')
          
    if lives == 0:
        print(f'you died, the word is {word}')
    else:
        print(f'Congrat! you guessed the word {word}.')

            
            
if __name__ == '__main__':
    hangman()
            