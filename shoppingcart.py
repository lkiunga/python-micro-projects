
shopping_cart = {}
shopping_cart["Biscuits"] = 10
shopping_cart["chocolates"] = 25

#Get user to add items to the dictionary
for i in range(2):
    item_name = input("Enter name of the product ")
    item_price = int(input("Enter the price of the product = "))

    shopping_cart[item_name] = item_price

print(shopping_cart)
# remove an item from the list
#item_remove = input("Item to remove from shopping list ")
#del shopping_cart[item_remove]

# print out each item name and price
print(shopping_cart)
total_sum = 0

# sum up the prices in a dictionary
#Dict-name.keys() allows to iterate and return on oly the keys
#Dict-name.values() allows us to iterate over adictionary anf return only the values
for key, value in shopping_cart.items():
    total_sum += shopping_cart[key]
    #print (total_sum)
# print the total sum 
  
print(" the total sum is Ksh ", total_sum)


for product,price1 in shopping_cart.items():
    print("The price os {} is Ksh {}.00".format(product, price1))
#dictionary.items(). This method returns a tuple for each element in the dictionary,
#  where the first element in the tuple is the key and the second is the value.
#dictionary.keys()
#dictionary.values().