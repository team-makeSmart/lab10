# Lab 10 CST205 MODULE 4
# Team MakeSmart
# Jake McGhee, Mac Doussias, Pavlos Papadonikolakis
# 11-19-17

#TODO Secondary objective, add exception handling to all function, if time permits.

# Warm Up
def getName():
  """ Prompts user to enter a string that represents their name. """  
  return requestString("What is your name?")
    
def wordLoop():
  """ Continuously gets user to enter word, then prints word std output. Breaks loop when user presses 'stop' or 'cancel'."""
  #TODO time permitting, handle the exception of pressing the cancel button so it doesn't throw an error.
  word = ''
  while (word != "stop"):
    word = requestString("Enter a word or type \'stop\' to stop")
    print word.lower()

# Hangman

def hangman():
    from random import randint
    
    # TODO add description of game
    # print description
    
    # TODO add more words to the word bank
    wordBank = ["CAT"]
    word = wordBank[randint(0, len(wordBank) - 1)]
    
    guessesLeft = 6
    lettersGuessed = []
    guessedWord = ""
    
    while (guessesLeft > 0 and guessedWord != word):
    
        
        # get new letter
        guess = requestString("Guess a letter: ").upper()
        # TODO make sure input is a single character
        # TODO make sure letter has not been guessed already
        if (not guess in word):
            guessesLeft -= 1
            # TODO add functions for drawing the hangman
            if (guessesLeft > 0):
                print ("Guesses Left: %s" % guessesLeft)
        lettersGuessed.append(guess) 
        
        if (guessesLeft > 0):
            # create encrypted word
            encryptedWord = []
            for letter in word:
                if letter in lettersGuessed:
                    encryptedWord.append(letter)
                else:
                    encryptedWord.append("_")
            encryptedWordString = " ".join(encryptedWord)
            guessedWord = "".join(encryptedWord)
            print encryptedWordString
        
    if (guessedWord == word):
        print "You win!"
    else:
        print "You lose!"
        
    
        
        
  
    
    
