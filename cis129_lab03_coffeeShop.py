# asking the user how many coffees and muffins they would like to purchase
numberOfCoffees = int(input('How many coffees would you like to purchase?'))
numberOfMuffins = int(input('How many muffins would you like to purchase?'))

# making the receipt based on what user inputed
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of Coffees bought?')
print(numberOfCoffees)
print('***************************************')
print('Number of Muffins bought?')
print(numberOfMuffins)

# Mutplying items bought with their prices
print('***************************************')
print('My Coffee and Muffin Shop Recipt')
print(str(numberOfCoffees) + ' Coffees at $5 each: $' + str(numberOfCoffees * 5) )
print(str(numberOfMuffins) + ' Muffins at $4 each: $' + str(numberOfMuffins * 4) )

# setting variables to show taxes
coffeeCost = numberOfCoffees * 5 
muffinCost = numberOfMuffins * 4
totalCost = coffeeCost + muffinCost
tax = totalCost * 0.06
totalCostWithTax = totalCost + tax

# final portion of recipt 
print(str('6% tax: $') + str(tax))
print('---------')
print(str('Total: $') + str(totalCostWithTax))
print('***************************************')
