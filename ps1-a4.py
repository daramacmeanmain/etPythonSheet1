#Solution for Factorial Digit Sum

import math

#calculation for 100! (line of code from https://stackoverflow.com/questions/3411657/calculating-factorial-in-python)
fact = math.factorial(100)
print ("100! is", fact)

#output the sum of the factorial digits (line of code from https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python)
print ("Sum of the digits of 100! is", sum(int(digit) for digit in str(fact)))