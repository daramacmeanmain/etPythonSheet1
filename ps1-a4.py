#Solution for Factorial Digit Sum

import math

#calculation for 100! (line of code from https://stackoverflow.com/questions/3411657/calculating-factorial-in-python)
fact = math.factorial(100)

#output the sum of the factorial digits (line of code from https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python)
print (sum(int(digit) for digit in str(fact)))