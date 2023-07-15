# Key and pairs 
#Uses {}
# Dictionaries are mutable 
#my_dictionarySyntax = {keyA:value1,value2, keyB:value3,value4}
#len(dictionary) - Returns the number of items in a dictionary.
#for key, in dictionary - Iterates over each key in a dictionary.
#for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.
#if key in dictionary - Checks whether a key is in a dictionary.
#dictionary[key] - Accesses a value using the associated key from a dictionary.
#dictionary[key] = value - Sets a value associated with a key.
#del dictionary[key] - Removes a value using the associated key from a dictionary.

#Task 1 
#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
#generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
	emails = []
	for domain, users in domains.items():
		for user in users:
			emails.append(user+"@"+ domain)
			return emails
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


#Task 2
def groups_per_user(group_dictionary):
    user_groups = {}  # Dictionary to store user groups
    
    # Go through group_dictionary
    for group in group_dictionary.keys():
        # Now go through the users in the group
        for user in group_dictionary[group]:
            # Now add the group to the list of groups for this user, creating the entry in the dictionary if necessary
            if user in user_groups:
                # User already exists in the dictionary, append the group to their existing list
                user_groups[user].append(group)
            else:
                # User doesn't exist in the dictionary, create a new list with the current group
                user_groups[user] = [group]
    
    return user_groups

# Example usage
print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
