# asking the user how many coffees and muffins they would like to purchase
numberOfCoffees = int(input('How many coffees would you like to purchase?'))
numberOfMuffins = int(input('How many muffins would you like to purchase?'))
numberOfDonuts = int(input('How many donuts would you like to purchase?'))
numberOfTeas = int(input('How many teas would you like to purchase?'))

# making the receipt based on what user inputed
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of Coffees bought?')
print(numberOfCoffees)
print('***************************************')
print('Number of Muffins bought?')
print(numberOfMuffins)
print('Number of Donuts bought?') 
print(numberOfDonuts) 
print('Number of Teas bought?')
print(numberOfTeas)

# Mutplying items bought with their prices
print('***************************************')
print('My Coffee and Muffin Shop Recipt')
print(str(numberOfCoffees) + ' Coffees at $5 each: $' + str(numberOfCoffees * 5))
print(str(numberOfMuffins) + ' Muffins at $4 each: $' + str(numberOfMuffins * 4))
print(str(numberofDonuts) + ' Donuts at $3 each: $' + str(numberOfDonuts * 3))
print(str(numberOfTeas) + ' Teas at $4 each: $' + str(numberofTeas * 4))

# setting variables to show taxes
coffeeCost = numberOfCoffees * 5 
muffinCost = numberOfMuffins * 4
donutCost = numberOfDonut * 3
teaCost = numberOfTea * 4
totalCost = coffeeCost + muffinCost + donutCost + teaCost
tax = totalCost * 0.06
totalCostWithTax = totalCost + tax

# final portion of recipt 
print(str('6% tax: $') + str(tax))
print('---------')
print(str('Total: $') + str(totalCostWithTax))

print('Thank you for shopping at our coffee shop, have a nice day!!')
print('***************************************')
