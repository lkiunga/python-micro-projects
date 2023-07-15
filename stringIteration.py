#Strings are sequences of characters, and are immutable
#Task is to convert strings to how they would be written by Jayden smith - unique wtiting style of Capitalizing the strat of every word in a sentence
#Input String
jaydenQuote = "How can mirrors be real if our eyes aren't real"
print (jaydenQuote)
#Split the string into a list of words seperated by the space
words = jaydenQuote.split()
print(words)
#Strings are immutable hence we need to store them as list since list are mutable
#create an empty list to store the capitalized words
capitalizeJaydenWords = []
#Iterate over each word in the words list
for word in words:
    #Capitalize the word
    capitalizeJaydenWord= word.capitalize()
    #Add it to the capitalized list
    capitalizeJaydenWords.append(capitalizeJaydenWord)
    
#Join the capitalized words into a single string
#Join syntax - string.join(iterable) - The string is the seperator for the iterable
jaydenQuoteCase = " ".join(capitalizeJaydenWords)
print (jaydenQuoteCase)

#Task 2 
def pig_latin(text):
  say = ""
  # Separate the text into words
  pigilatin = []
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:]+ word[0]+ 'ay'+ ' '
    # Turn the list back into a phrase
    

  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"