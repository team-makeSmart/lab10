# Lab 10 CST205 MODULE 4
# Team MakeSmart
# Jake McGhee, Mac Doussias, Pavlos Papadonikolakis
# 11-19-17



# Warm Up
def getName():
    """ Prompts user to enter a string that represents their name. """
    return requestString("What is your name?")


def wordsLoop():
    """ Continuously gets user to enter words, then prints words std output. Breaks loop when user presses 'stop' or 'cancel'."""

    words = ''
    while (words != "stop"):
        words = requestString("Enter a words or type \'stop\' to stop")
        print words.lower()


# Hangman
def hangman():

    print'\t\t\t  DESCRIPTION\n' \
         '-----------------------------------------------------------------------------\n' \
         '- In this game the computer selects randomly a words from a list of wordss and the player\n- tries to guess it' \
         ' by suggesting letters.If the guessing player suggests a letter which occurs\n- in the words, the letter appears' \
         ' in its correct position.The program allows the user to make\n- a total of 6 guesses. ' \
         ' If the suggested letter does not occur the player looses 1 of the 6\n- guesses.' \
         ' If the player quesses all the letters s/he wins else s/he looses the game.\t\n' \
         ' ----------------------------------------------------------------------------'

    words = 'THE GOOD THE BAD AND THE UNGLY'      
    guessesLeft = 0
    lettersGuessed = []
    wrongGuessed = []
    guessedwords = ""
    encryptedwords = [] 
    for i in xrange(len(words)):
      if words[i].isalpha():
        encryptedwords.append(' _ ')
      elif words[i] == ' ':
        encryptedwords.append('   ')

    for i in xrange(len(encryptedwords)):
        print encryptedwords[i],     

    wholePhrase = ''

    while (guessesLeft != 6 and wholePhrase != getTrimmedwords(words)):

        guess = requestString("Guess a letter: ").upper()  # get guess from user
        guessesLeft = checkError(guess, lettersGuessed, words, wrongGuessed, guessesLeft)
        lettersGuessed.append(guess)
        wholePhrase = wordsSofar(words, guess, encryptedwords)

        if len(wrongGuessed) > 0:
            print'\nIncorrect guesses:'
            for letter in wrongGuessed:
                print letter,  # comma to print in one line

        print ("\nYou have used %s of six guesses " % guessesLeft)

    if wholePhrase == getTrimmedwords(words):
        print "You win!"
    else:
        print "You lose!"


def checkError(guess, lettersGuessed, words, wrongGuessed, guessesLeft):
    """ checks the user's input, if correct guess, it prints correct """
    """ otherwise it prints incorrect """

    """ words:(string) the words to guess"""
    """ guess:(string) the letter guessed """
    """ lettersGuessed:(list) the list of guessed letters """
    """ wrongGuessed:(list) the list of wrong guessed letters """
    """ guessesLeft:(int) the guesses left """

    if (len(guess) != 1):
        print "Error!  Only enter one character to guess from words."
    elif not guess.isalpha():
        print 'Letters only please!'
    elif (guess in lettersGuessed):
        print "You already guessed " + str(guess)
    elif (not guess in words and guess.isalpha()):
        guessesLeft += 1
        wrongGuessed.append(guess)
        print '\nIncorrect!'
    else:
        print '\nCorrect!'
    return guessesLeft


def wordsSofar(words, guess, encryptedwords):
    """ prints what is guessed so far """

    """ words:(string) the words to guess"""
    """ guess:(string) the letter guessed """
    """ lettersGuessed:(list) the list of guessed let
    ters """

    str = ''
    for i in xrange(len(words)):
        if words[i] == guess:
            encryptedwords[i] = guess

    print 'words so far:'
    for i in xrange(len(encryptedwords)):
        print encryptedwords[i],
        str += encryptedwords[i]

    return getTrimmedwords(str)


def getTrimmedwords(words):
    trimmed = ''
    for i in xrange(len(words)):
        if words[i] != ' ':
            trimmed += words[i]
    return str(trimmed)
