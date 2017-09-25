import random

r = random.randrange(1,10)
user = 0
count = 0

def guess():
	user = int(input("Enter number between 1 and 10:"), 16)
	if user < r:
		print("Number too low")
	elif user > r:
		print("Number too high")
	else:
		print("Correct, the number is", r)
	return
			
while user != r:
	count += 1
	guess()
	
print ("Number of tries:", count)