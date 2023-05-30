# Creating  two story - one with static variables and the other with Dynamic variables
print("Story 1")
story1 = "Welcome to Azubi Africa. Please enter your group members names. name 1 or name 2"
print(story1.upper())
print(story1.lower())
print(story1.capitalize())
print(story1.count("a"))
#Getting information from the user
# userInput1 = input("Enter name 1 or name 2 ")
# userInput2 =input("Enter name 1 or name 2")
# userInput3 = input("Enter name 1 or name 2")
# print ("story 2")
# print("Welcome to Azubi Africa! Please enter your group members names. "+ userInput1.capitalize())
# print(f"Welcome to Azubi Africa! Please enter your group members names. {userInput1} or {userInput2}")
# print("Welcome to Azubi Africa! Please enter your group members names. "+ userInput1 + " or "+ userInput2 + " or "+ userInput3)
#print Blank lines  us /n or an empyt print()
#Printing statements as debugging tool they help ffcfshow where the work is stopping at
print("Python Data Types")
x= 23
print (type(x))
y = 23.8
print (type(y))
int(y)
print(y)
print (str(y) ,"dollares")
print('Press "enter"')

#Collections - List[] and array- collection of diffent data types
scores = []
scores.append(98)
print(scores)
print(len(scores))
scores.insert(0,"Bill")
#scores.sort()# modifies the list
print(scores)
print(scores[1:3])# starting index but not including last index
#Array = numerical data types and mustt all be the same
#Lists = store anything and any data type - guranteed order
#results = array("Englis =")


#Dictionaries - Key value pairs - storage order not Guranteed
linet ={}
linet ['First'] = 'Linet'
linet['last'] = 'Kendi'

tinel ={}
tinel ['First'] = 'Tinel'
tinel['last'] = 'Pendo'

students = []
students.append(linet)
students.append(tinel)
students.append({
    'First':'Anaia', 'last' : 'Mapenzi'
})
print(students)