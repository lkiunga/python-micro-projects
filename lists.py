# Lists are sequence of elements of any data type, and are mutable
#List and Strings are sequences
# Lists are mutable hence can be modified while strings are immutable 
#create a list
cars = ["BMW", "TOYOTA", "HONDA", "LEZUS", "SUBARU"]
print(cars)
#adds to the end of the list
cars.append("NISSAN")
print(cars)
# insert - a particular places 
cars.insert(2, "MERCEDEZ")
print(cars)
#remove - used to remove from the list
cars.remove("HONDA")
print(cars)
#pop methos which recives an index
cars.pop(3)
print(cars)
#changing the contents of list
cars[1] = "MAZDA"
print(cars)
# Sorts the items in the list 
cars.sort()
print("sorted:", cars)
# reverse the items in a list
cars.reverse()
print(cars)

#Iterate though a list
animals = ["Lion", "Zebra","Dolphin", "Monkey"]
chars = 0
for animal in animals:
    #len of the name of one animal combined with others in the string
    chars += len(animal)
print("Total characters:{}, Average lengths: {}".format(chars, chars/len(animals)))
# total number of animals in the animal list

#Extend a new list
cars.extend(animals)
print(cars)

#List Comprehension


def odd_numbers(n):
	return [x for x in range(n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

def squares(start, end):
    return [ n*n  for n in range (start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]

def group_list(group, users):
  
  return group +": "+", ".join(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:

