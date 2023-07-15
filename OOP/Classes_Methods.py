#print (dir(int))

#print(help(int))

class Piglet:
    name = "piglet"
    years = 0
    def speak(self):
        print("Oink! I'm {}! Oink!". format(self.name))
    def pig_years(self):
        return self.years * 18
# self which represents the instance the method is being executed on -allow you to access attributes of the instance using dot notation, like self.name 
hamlet = Piglet()
hamlet.name = "hamlet"
hamlet.years = 12
print(hamlet.speak())
print(hamlet.pig_years())

petunia = Piglet()
petunia.name = "shady"
print(petunia.speak())

#Example of a Constructors
class Person:
    #Constructor speciale name is __init__
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "This is instance {}".format(self.name)
    def greeting(self):
        """Output the greetings for the person"""
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Jonah")  
# Call the greeting method
print(some_person.greeting())
print(some_person)
help(Person.greeting)

#__str__ - method for instances or objects that you want to print all ther values
#Docstring - added to classes, methods and functions 
