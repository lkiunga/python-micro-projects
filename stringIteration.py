#Task is to convert strings to how they would be written by Jayden smith - unique wtiting style of Capitalizing the strat of every word in a sentence
#Input String
jaydenQuote = "How can mirrors be real if our eyes aren't real"
print (jaydenQuote)
#Split the string into a list of words seperated by the space
words = jaydenQuote.split()
print(words)
#create an empty list to store the capitalized words
capitalizeJaydenWords = []
#Iterate over each word in the words list
for word in words:
    #Capitalize the word
    capitalizeJaydenWord= word.capitalize()
    #Add it to the capitalized list
    capitalizeJaydenWords.append(capitalizeJaydenWord)
    
#Join the capitalized words into a single string
jaydenQuoteCase = " ".join(capitalizeJaydenWords)
print (jaydenQuoteCase)