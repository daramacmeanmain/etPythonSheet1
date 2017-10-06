#Reverse String

#User inputs word to reverse
word = input("Enter a word: ")

#Creates a reversed string of the word (code for outputting string adapted from https://stackoverflow.com/questions/28632804/why-strreversed-doesnt-give-me-the-reversed-string)
reversedWord = ''.join(reversed(word))

#output the reversed string
print(reversedWord)