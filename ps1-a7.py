#Test whether or not a string is a palindrome

#User inputs word for palindrome test
word = input("Enter a word: ")
#Word converted to case insensitive 
word = word.casefold()
#Creates a reversed string of the word
reversedWord = reversed(word)

#Determine whether the word is a palindrome or not, and output the result
if list(word) == list(reversedWord):
	print("That word is a palindrome")
else:
	print("That word is not a palindrome")