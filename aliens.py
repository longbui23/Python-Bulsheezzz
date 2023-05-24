#Christine and Long

#ask users for number of Aliens and number of Weeks
numAliens=input("How many aliens have landed? >>")
numWeeks=input("How many weeks have passed since the aliens landed? >>")

#loop to count and print out number of aliens each week
for counter in range(1, int(numWeeks)+1):
	numAliens = int(numAliens)*2
	print("In week ", counter, " there are ", numAliens, " aliens on Earth.")