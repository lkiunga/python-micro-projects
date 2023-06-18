#Defining while loop examples
#Functon the counts the numer of integer factors for a givenNumber  variable 
# print outthe factor of he number

def countFactors(givenNumber):
    factor = 1
    count = 1
    if givenNumber == 0:
        return 0
    while factor < givenNumber:
        if givenNumber % factor == 0:
            count  += 1
            print("The factors of",givenNumber,"are ",factor)

        else:
            #prints The numbers that are not prime Factors
            print(factor)
        factor += 1
    return count

#print (countFactors(3))
#print (countFactors(12))
#print(countFactors(10))
#print (countFactors(24))
print(countFactors(100))