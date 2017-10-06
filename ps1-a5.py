#Guessing Game
#Unfinished - program doesn't stop

import random

#generate random number
r = random.randrange(1,10)
user = 0
count = 0

#determine whether the user input number is lesser than, greater than or equal to the random number
def guess():
	user = int(input("Enter number between 1 and 10:"), 16)
	if user < r:
		print("Number too low")
	elif user > r:
		print("Number too high")
	else:
		print("Correct, the number is", r)
	return

#count the number of turns the user takes	
while user != r:
	count += 1
	guess()

#output the number of turns	
print ("Number of tries:", count)