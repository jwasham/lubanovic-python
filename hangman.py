# Hangman game

import random
import string

def loadWords(wordfile):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print "Loading word list from file..."
    # inFile: file
    inFile = open(wordfile, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    # print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    word_set = set(secretWord)
    guessed_set = set(lettersGuessed)

    difference = set(word_set) - set(guessed_set)

    return len(difference) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    guessed = set(lettersGuessed)
    output = []

    for index in range(len(secretWord)):
        if secretWord[index] in guessed:
            output.append(' ' + secretWord[index] + ' ')
        else:
            output.append(' _ ')

    return ''.join(output)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    letter_list = list(string.ascii_lowercase)

    for letter in set(lettersGuessed):
        letter_list.remove(letter)

    return ''.join(letter_list)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_left = 8
    guessed_letters = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))

    complete = False

    while not complete:
        print('------------')
        print('You have {} guesses left'.format(guesses_left))
        print('Available Letters: {}'.format(getAvailableLetters(guessed_letters)))

        guess_raw = raw_input('Please guess a letter: ')
        guess = guess_raw.lower()

        if guess in guessed_letters:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, guessed_letters))
        else:
            guessed_letters.append(guess)

            if isWordGuessed(secretWord, guessed_letters):
                print('Good guess: ' + secretWord)
                print('------------')
                complete = True
                print('Congratulations, you won!')
            elif guess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, guessed_letters))
            else:
                guesses_left -= 1

                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, guessed_letters))

                if guesses_left == 0:
                    print('------------')
                    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
                    complete = True



# wordlist = loadWords('words.txt')
# secretWord = chooseWord(wordlist).lower()
#
# hangman(secretWord)

