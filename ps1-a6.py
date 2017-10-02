#Find the largest and smallest element in a list

print("Enter a series of numbers, separated by spaces")
#user input for multiple integers (line of code from https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user)
num = [int(x) for x in input().split()]

#output the largest number in the user generated list followed by the smallest 
print("The largest number is", max(num))
print("The smallest number is", min(num))