#The enumerate() fuction takes a list as a parameter and returns a tuple of each element in the list.
#the first value of the tuple is the index amd the second value is the element itself


#Complete the skip_elements function to return every other element from the list,
#this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
	# code goes here
	newList = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			newList.append(element)
	
	return newList

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']