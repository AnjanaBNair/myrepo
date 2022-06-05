# mad_libs_game.py - A Mad Libs game.

import string                       # For string.punctuation
from re import findall              # To create a list of words displayed to the screen

import mad_libs_library as mlib     # Script containing the sentences for the game play
import random                       # For random.shuffle

# Shuffle the sentences in mad_libs_library
random.shuffle(mlib.mad_libs)

key_words = ['ADJECTIVE', 'NOUN', 'PRONOUN', 'INTERJECTION', 'EXCLAMATION', 'VERB', 'ADVERB']

for sentence in mlib.mad_libs:
    print(sentence)

    # List containing words and punctuation marks of the current sentence on the screen
    words = findall(r'\w+|["!#$()\[\]%&\'./:?;,<=>]', sentence)
    key_words_found = []            # List to contain keywords found in current sentence

    # Adding keywords found in sentence to key_words_found list
    for word in words:
        if word in key_words:
            key_words_found.append(word)

    # Ask for user's input and replace the keywords with user's input
    for word in key_words_found:
        user_choice = input('Enter a(n) ' + word + ': ')
        words.insert(words.index(word), user_choice)
        words.remove(word)

    # Combine words and print new sentence
    new_sentence = ''       # Variable to contain sentence formed based on user's input
    for word in words:
        if word in string.punctuation or word is words[0]:
            new_sentence += word

        else:
            new_sentence += ' ' + word

    print(new_sentence, '\n')
