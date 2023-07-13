# use tuples to store information about a file: its name, its type and its size in bytes
#Tuples are fized mutable elements and can store data of different types
def file_size(file_info):
	file_name, file_type, size_bytes= file_info
	return("{:.2f}".format(size_bytes / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21