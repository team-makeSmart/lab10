
# Lab 10 CST205 MODULE 4
# Team MakeSmart
# Jake McGhee, Mac Doussias, Pavlos Papadonikolakis
# 11-19-17



# Warm Up
def getName():
  """ Prompts user to enter a string that represents their name. """  
  return requestString("What is your name?")
    
def wordLoop():
  """ Continuously gets user to enter word, then prints word std output. Breaks loop when user presses 'stop' or 'cancel'."""

  word = ''
  while (word != "stop"):
    word = requestString("Enter a word or type \'stop\' to stop")
    print word.lower()

    

# Hangman
def hangman():
    from random import randint
    
    print'\t\t\t  DESCRIPTION\n'\
         '-----------------------------------------------------------------------------\n'\
         '- In this game the computer selects randomly a word from a list of words and the player\n- tries to guess it' \
         ' by suggesting letters.If the guessing player suggests a letter which occurs\n- in the word, the letter appears' \
         ' in its correct position.The program allows the user to make\n- a total of 6 guesses. ' \
         ' If the suggested letter does not occur the player looses 1 of the 6\n- guesses.' \
         ' If the player quesses all the letters s/he wins else s/he looses the game.\t\n'\
         ' ----------------------------------------------------------------------------' 

    
    wordBank = ["CAT", "AARDVARK","JAZZ"]
    word = wordBank[randint(0, len(wordBank) - 1)]
    guessesLeft = 0
    lettersGuessed = []
    wrongGuessed = []
    guessedWord = ""
    
    while (guessesLeft != 6 and guessedWord != word):
    
        guess = requestString("Guess a letter: ").upper() #get guess from user   
        guessesLeft = checkError(guess,lettersGuessed,word,wrongGuessed,guessesLeft)      
        lettersGuessed.append(guess)
        guessedWord = printWordSofar(word,guess,lettersGuessed)    
        
        if len(wrongGuessed) > 0:
          print'Incorrect guesses:'
          for letter in wrongGuessed:
            print letter, # comma to print in one line     
                
        print ("\nYou have used %s of six guesses " % guessesLeft)
       
    if (guessedWord == word):
      print "You win!"
    else:
      print "You lose!"
        
        
        
def checkError(guess, lettersGuessed, word, wrongGuessed, guessesLeft):
  """ checks the user's input, if correct guess, it prints correct """
  """ otherwise it prints incorrect """
  
  """ word:(string) the word to guess"""
  """ guess:(string) the letter guessed """
  """ lettersGuessed:(list) the list of guessed letters """
  """ wrongGuessed:(list) the list of wrong guessed letters """
  """ guessesLeft:(int) the guesses left """
  
  if( len(guess) != 1):  
    print "Error!  Only enter one character to guess from word."
  elif not guess.isalpha() :
    print 'Letters only please!'
  elif(guess in lettersGuessed):
    print "You already guessed "+str(guess)  
  elif (not guess in word and guess.isalpha()):
    guessesLeft += 1
    wrongGuessed.append(guess)
    print 'Incorrect!'
  else:
    print 'Correct!'
  return  guessesLeft     
  
                                    
def printWordSofar(word,guess,lettersGuessed):
  """ prints what is guessed so far """
 
  """ word:(string) the word to guess"""
  """ guess:(string) the letter guessed """
  """ lettersGuessed:(list) the list of guessed letters """

  encryptedWord = []
        
  for letter in word:
    if letter in lettersGuessed:
      encryptedWord.append(letter)
    else:
      encryptedWord.append(" _ ")   
    encryptedWordString = "".join(encryptedWord)

  print 'Word so far:'
  print encryptedWordString
  return encryptedWordString
