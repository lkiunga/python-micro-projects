#Tip Calculator
# the program should calculate the total amoun of a meal purchased with a fixed tip
foodCharge = float(input("Enter the Charge for food = "))
#print(type(foodCharge))
tipPercentage = 0.18
tip = tipPercentage *foodCharge
print(f"Tip = ${'%.2f' % tip}")

sTaxPercentange = 0.07
salesTax = sTaxPercentange * foodCharge
print(f"Sales Tax = ${'%.2f' %salesTax}")
#trying to keep up with the sharing and chasing the greenlight
total =foodCharge + tip + salesTax
print(f"Grand Total = ${'%.2f'% total}")
print(3+5.0)