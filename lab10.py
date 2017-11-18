# Lab 10
# Team MakeSmart

# Warm Up

def getName():
    return requestString("What is your name?")
    
def wordLoop():
    word = ''
    while (word != "stop"):
        word = requestString("Enter a word or type stop to stop")
        word.lower()

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
        
    
        
        
  
    
    