#Christine and Long

#Ask the user items
items=int(input("How many items? >>"))

#int var for maxPrice and minPrice
maxPrice=float(input("Enter the price: "))
minPrice= maxPrice

#loop to ask price for each item
for item in range(items-1):
	price = float(input("Enter the price:  "))

	#compare and attach the fittest value to maxPrice and minPrice
	maxPrice=max(maxPrice, price)
	minPrice=min(minPrice, price)

#print highest price and lowest price
print("The highest price item costs ", maxPrice)
print ("The lowest price item costs ", minPrice)