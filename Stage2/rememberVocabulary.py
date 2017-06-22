# guess Vocabulary game
gameDifficulty = raw_input('''\n\nPlease select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.\n''')




if (gameDifficulty == 'easy'):
	sample = '''A common first thing to do in a language is display
'Hello ___1___!' In ___2___ this is particulary easy; all you have to do 
is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an 
example of how to output to the user using the ___3___ command, and
produces a program which does soemthing, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's 
a step in learning ___2___ syntax, and that's really its purpose.'''
	blanksList = ['___1___','___2___','___3___','___4___']
	answers = ['World','python','print','html']
elif(gameDifficulty == 'medium'):
	sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
on't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
	blanksList = ['___1___','___2___','___3___','___4___'] 
	answers = ['function','arguments','none','list']
else:
	gameDifficulty = 'hard'
	sample = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''
	blanksList = ['__1__','__2__','__3__','__4__','__5__','__6__','__7__','__8__','__9__','__10__']
	answers = ['class','method','__init__','instance','__repr__','__add__','__sub__','__lt__','__gt__','__eq__']

print "You've chosen "+ gameDifficulty +'!'

def word_in_pos(word, listOfBlanks):
	#searches for blank of listOfBlanks in word
	#input: word [string], listOfblanks [list of strings] 
	#outpu: string or None
	counter_listOfBlanks = 0
	while( counter_listOfBlanks <= len(listOfBlanks) ):
		if(word.find(listOfBlanks[ counter_listOfBlanks ]) >= 0 ): # other way: listOfBlanks[ counter_listOfBlanks ] == word
			return listOfBlanks[ counter_listOfBlanks ]
		counter_listOfBlanks += 1
		return None

def blanks_in_text(bigStringText, listOfBlanks):
	# revelas if blanks are found in bigStringText [string]
	# input: listOfBlanks [list of strings]
	# outpu: blanksExistance [bool]
	blanksExistance = False
	for word in listOfBlanks:
		if (bigStringText.find(word) >= 0):
			blanksExistance = True
			return blanksExistance
	return blanksExistance

def myTextStatusPrint(sample):
	# avoiding repetion code - 
	# output: string with the "big" text
	return '\nThe current paragraph reads as such:\n' + sample

maxGuesses = raw_input('''\nHow many guesses do you like for each guess?\n''')
maxGuesses = int(maxGuesses)

#loop ***
win = False
forceOutOfOuterloop = False # change to False when guessing wrong 5 timess
blankIndex = 0
while( blanks_in_text(sample, blanksList) and not forceOutOfOuterloop  ): #blanks_in_text(sample, blanksList) 
	print myTextStatusPrint(sample)
	guesses_left = maxGuesses   # reinitilize masGuesses for each new blank
	while( 0 < guesses_left ):
		if(guesses_left != maxGuesses):
			print myTextStatusPrint(sample)
		input_prompt = raw_input('\nWhat should be substituted in for'+ blanksList[blankIndex] +'? ')
		if ( input_prompt == answers[blankIndex] ): # correct guess
			sample = sample.replace(blanksList[blankIndex], answers[blankIndex])
			if (blankIndex ==  len(blanksList)-1 ):
				print myTextStatusPrint(sample)	
			print 'Correct !'
			break # jumps out of: while( 0 < guesses_left ):
		else:                                       # faild guess
			guesses_left -=1
			if (guesses_left != 0 and guesses_left != 1 ):
				print "\nThis isn't the correct answer! Let's try again; you have " + str(guesses_left)+ " trys left!"
			if(guesses_left == 1):
				print "\nThis isn't the correct answer! Let's try again; you have " + str(guesses_left)+ " trys left! Make it count!"
		if (guesses_left == 0):                      # failed 5 guesses # stays: win = False - player loses
			forceOutOfOuterloop = True  # break out of outer loop -  while( blanks_in_text(sample, blanksList) and not forceOutOfOuterloop  ):
			break                       # break from the nested while loop - while( 0 < guesses_left ):
	if ( (len(blanksList)-1) == blankIndex ): # went/guessed through blank all cases
		win = True
	blankIndex += 1

# prints the result

if (win):
	print "\nYou won!\n"
else:
	print "\nYou've faild too many straight guesses! Game over!\n"





