#Solution for FizzBuzz Problem

#Loop from 1 to 100
for i in range (1, 101):
#check if number is a multiple of both 3 and 5, and print FizzBuzz
	if i % 3 == 0 and i % 5 == 0:
		print ("FizzBuzz")
#check is number is a multiple of 3 and print Fizz		
	elif i % 3 == 0:
		print("Fizz")
#check if number is a multiple of 5 and print Buzz
	elif i % 5 == 0:
		print ("Buzz")
#otherwise print number
	else:
		print (i)