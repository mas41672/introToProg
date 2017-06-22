 # IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?
# The answer for ___2___ is 'arguments'. 
# The answer for ___3___ is 'none'.
# The answer for ___4___ is 'list'. 

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
#print sample1

blanksList1 = ['___1___','___2___','___3___','___4___','___5___']
answers1 = ['function','parameters','none','lists']

# Checks if a blank of the string list blanks is a substring of the string word passed from sample1 
def checkForBlank_in_word(word, blanksList):   # answer needed for if-else sequence
	#checks if string named word contains a blank as a substring
	#input: blanksList - list of the blanks; ___#number___
	#ouput: returns the blank if found or else returns None
	for specificBlank in blanksList:
		if 0 <= word.find(specificBlank):
			return specificBlank
		return None

def promptUserAndCheckAnswer(sample, word, blanksList, answer, blankIndex): 
	# function prompts the user and checks answer until correct answer
	# it also fills in the 
	# or output status 
	# input: sample, word, blankList, answer1, blankIndex
	# outuput: True or False/ boolean variable
	print sample
	boolStopGame = True
          # here or outside ???????????????????????????????????????????
	count = 5  # five guesses
	while count > 0:
		# code of loop 
		if count > 0:
			user_input = raw_input("What should be substituted in for " + blanksList[blankIndex]+"? ")
		# check for correct answer and change boolStopGame
		if (answer[blankIndex]==user_input):
			# check for correct answer and change boolStopGame flag 
			count = 0
			boolStopGame = False
		 	# refresh sample
		count -=1
	return boolStopGame, blankIdex

# Plays a guessing game. !!!!!!!!!!!! blankIndex
def play_game(sample, blanksList,answer):
	#game for learning vocabulary
	#input: text in string variable sample
	#input: blanks in list of strings named 'blanksList'
	#outpu: text with blanks filled in by user
	blankIndex = 0
	sample_splited = sample.split()
	for word in sample_splited:
		answerFunction = checkForBlank_in_word(word, blanksList)
		if answerFunction != None:
			count = 5  # five guesses
			while count > 0:
				# code of loop 
				if count > 0:
					user_input = raw_input("What should be substituted in for " + blanksList[blankIndex]+"? ")
				# check for correct answer and change boolStopGame
				if (answer[blankIndex]==user_input):
					# check for correct answer and change boolStopGame flag 
					count = 0
					boolStopGame = False
				 	# refresh sample
				 	sample = sample.replace(blanksList[blankIndex],answer[blankIndex])
				count -=1
			#boolStopGame, blankIndex = promptUserAndCheckAnswer(sample, word, blanksList, answer, blankIndex)
	return sample
	# 			blankIndex += 1

print play_game(sample1,blanksList1,answers1)