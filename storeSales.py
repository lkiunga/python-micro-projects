"""
Azubi store has products that customers love; Given are the products, prices and the number of customers that purchased products last week
Azubi stores wants to be able to do the following calculations on the data.
The following is the criteria
1. calculate the total price average for all products
2. Create a new price list that reduces the old prices by $5
3. Calculate the total revenue generated from the products
4. calacluate the average daily avenue generaed from the products
5. Based on te new prices, which products are less than $ 30
"""
priceList = {
    "Sankofa Foods": 30,
    "Jamestown Coffee":25,
    "Bioko Chocolate": 40,
    "Blue Skies Ice Cream": 20,
    "Fair Afric Chocolate": 20,
    "Kawa Moka Cofffee": 35,
    "Aphoro Spirit": 45,
    "Mensado Bissap": 50,
    "Voltic":35   
}

listKeys = priceList.keys()
print (listKeys)

lastWeekSales = [2,3,5,8,4,4,6,2,9]

totalPrice = 0

#1. calculate the total price average for all products
for price in priceList.values():
    totalPrice += price
averagePrice = totalPrice/len(priceList)
print('%.2f'% averagePrice )

#2. Create a new price list that reduces the old prices by $5
for newPrice in priceList.values():
    newPrice +=5
    
