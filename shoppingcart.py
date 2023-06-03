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
item_remove = input("Item to remove from shopping list ")
del shopping_cart[item_remove]

# print out each item name and price
print(shopping_cart)
total_sum = 0

# sum up the prices in a dictionary
for price in shopping_cart:
    

total_sum = shopping_cart[item_name] + total_sum
# print the total sum   
print(total_sum)
    