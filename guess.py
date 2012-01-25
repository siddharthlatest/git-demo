#This is our secret number
number = 7

n = input() #This is how you take input in python

while n != number:
    if n < number:
        print "Your guessed number is too small"
        print "Guess again"
        n = input()
    elif n > number:
        print "Your guessed number is too high"
        print "Guess again"
        n = input()

print "Great! You guessed our secret number ", number
