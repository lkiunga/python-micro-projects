#Tuples contain elements of any data type ad are immutable
#they ensure that the order of the data elements do not change 
#Use tuples to store information about a file: its name, its type and its size in bytes
#Tuples are fized mutable elements and can store data of different types
def file_size(file_info):
	file_name, file_type, size_bytes= file_info
	return("{:.2f}".format(size_bytes / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

#Storing the elements of a tuple in separate variables is called unpacking.
#This allows you to take multiple returned values from a function and store each value in its own variable.

def guest_list(guests):
	for guest in guests:
		guestName = guest[0]
		guestAge = guest[1]
		guestCareer = guest[2]

		print("{} is {} years old and works as {}".format(guestName,guestAge,guestCareer))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
