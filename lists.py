# List and Strings are sequences
# Lists are mutable hence can be modified while strings are immutable 
#create a list
cars = ["BMW", "TOYOTA", "HONDA", "LEZUS", "SUBARU"]
print(cars)
#adds to the eend of the list
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
