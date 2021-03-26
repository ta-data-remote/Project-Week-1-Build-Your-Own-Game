#!/usr/bin/env python
# coding: utf-8

# # The German Hangman Game
# Here you will find my awesome code for the ultrahard German Hangman Game.

# In[1]:


# START GAME
# user input "name" > all characters can be accepted
# print "Hi "name", are you ready to get owned by German Hangman?"
# wait 2 seconds, start game

# CHOOSE RANDOM WORD
# get a random word from word_list
# convert all words from word_list to upper case 
# store word in variable "word"

# GAMEPLAY FUNCTION
# set 10 tries (user can guess as much as he wants, but fail only 10 times)
# display the length of "word" to the user with _ _ _ underscores
# Hidden letters are shown as underscores, guessed letters will be unmasked
# prompt the user to guess a letter or word 
    # user input convert to uppercase always
# while loop until word is guessed or user runs out of tries
    # letter is in secret word > show letter in secret word, ask for user input again, show remaining tries, print "Nice try!"
    # letter is not in secret word > -1 try and ask for user input again, show remaining tries, print "This letter is not in the word, try again!"
# if user runs out of tries (10) and looses:
    # secret word is displayed, print ""name" you loose, guess you got owned by German hangman", start play again function
# if user wins or guesses the word right
    # word is displayed, print ""name" you win, you are ready to move to Berlin now!", start play again function
     
# PLAY AGAIN FUNCTION
# print "Are you ready to play again?"
# print "enter "Y" to start "N" 
    # make sure that only Y and N is possible (not weird other input > error message " wow you are already failing here"
    # gameplay function starts again

# possible problems with user input > error messages:
    # not a letter
    # same letter twice (show the user which letters he already used?)


# In[2]:


word_list = [
    'Heizoelrueckstoßabdaempfung',
    'Donaudampfschifffahrtskapitaensgeselltschaftsmuetzenhalterung',
    'Lokomotivdampfkesseldruckventilverschlussklappe',
    'Kirschkernweitspuckwettbewerb',
    'Weihnachtsmannschokoladeneinpackpapier',
    'Atmosphaere',
    'Destinationslebenszyklusmodell',
    'Desoxyribonukleinsaeure',
    'Papierschnipselchen',
    'Arbeitsunfaehigkeitsbescheinigung',
    'Hundehaftpflichtversicherung']


# In[3]:


import random


# In[4]:


import time


# In[5]:


#Start of the game

name = input("What is your name? ")

print ("Hello, " + name, "are you ready to get owned by German Hangman?")

time.sleep(2)

print ("Start guessing...")
print("\n")
time.sleep(1)


# In[21]:


#Functions

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play (word):
    word_completion = ("_" * len(word))
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5

    print(word_completion)
    print("\n")

    while guessed == False and tries > 0:    #guessed letter
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                print("\n")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                print("\n")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  #guessed word
            if guess in guessed_words:
                print("You already guessed the word", guess)
                print("\n")
            elif guess != word:
                print(guess, "is not the word.")
                print("\n")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            print("\n")
        print(word_completion)
        print("\n")
    if guessed:
        print("You win, you are ready to move to Berlin now!")
        print("\n")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
        print("\n")


def play_again():
    again = input("Ready to play Again? Input (Y/N) ").upper()
    print("\n")
    if again == "Y":
        play(word = get_word())
        play_again()
    elif again == "N":
        print("Ciao Kakao!")
    else:
        print("Y or N, no other input please...")
        print("\n")
        play_again()


# In[20]:


play(word = get_word())
play_again()


# In[ ]:




