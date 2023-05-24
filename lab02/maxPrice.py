#Christine and Long

#ask users for number of item
items=int(input("How many items? >>"))

#int var to maxPrice
maxPrice=float(input("Enter the price: >>"))

#loop to ask for price from each item
for item in range(items-1):
	price = float(input("Enter the price:  >>"))

	#compare and attach the fittest value to maxPrice
	maxPrice=max(maxPrice, price)

#print highest price
print("The highest price item costs ", maxPrice)