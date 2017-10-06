#Newton’s method for square roots

import math

x = 9
z = 0

#Output the actual quare root of x (in this case x = 9)
print("The square root of", x, "is", math.sqrt(x))
print()

#Loop through Newton's method 10 times and output the results
for z in range (1, 11):
	z_next = z - ((z*z - x) / (2 * z))
	print(z, "-", z_next)