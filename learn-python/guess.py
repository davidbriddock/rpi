# A number guessing game
# Created by David - July 2012

import random

# generate a random number between 1 and 20
def generate_number():
   return random.randint(1, 20)
   
# try to guess the number
def guess_number(number): 
   guessCount = 0  # start at zero
   
   # allow up to five attempts
   while guessCount < 5:      
      guessCount += 1  # add one
      
      guess = int(raw_input('Your guess? '))
      
      if guess == number:
         print "Success in {0} guesses!" . format(guessCount)
         return
      elif guess < number:
         print "Too low - try again..."
      elif guess > number:
         print "Too high - try again..."

   print "Too many guesses - the number was " + format(number)
   return

# find who is playing
name = raw_input("Who is playing today? ")

# guessing game loop
while True:
   print "\n" + name + " guess a number between 1 and 20"
   number = generate_number()   
   guess_number(number)
   
