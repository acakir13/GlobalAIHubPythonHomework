#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 


name = input('Please input your name:')
print('Welcome',name)


def get_word():
    words = ['bird', 'colur', 'country', 'school','family']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False
    
    print ('The word contains', len(word), 'letters.')
    print (len(word) * '*')
    while guessed== False and tries>0:
        print ('You  have ' + str(tries) +  ' tries')
        guess = input('Please enter letter of the full word.').lower()
        
        if  len(guess) == 1:
            if guess not in alphabet:
                print('you have not entered a letter.')
            elif guess in letters_guessed:
                print('you already have guessed that letter before')
            elif guess not in word:
                print('sorry, that letter is not part of the word')
                letters_guessed.append(guess)
            else:
                print ('No idea why we get this mesage, should be investigated further!')
        elif len(guess) == len(word) :
            if guess == word:
                print('Well done, you have guessed the word!')
                guessed= True
            else:
                print('sorry, that was not the word we were looking for')
                tries==1
                
            print ('The length of your guess is not the same as the length of the word we\'re looking for')
        statues = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
                    print(status)
                    
        if status == word:
            print ('Well done, you have guessed the word!')
            guessed = True
        elif tries==0:
            print ('you have run out of guesses and you haven\'t guessed the word.')
play_game()


# In[ ]:




