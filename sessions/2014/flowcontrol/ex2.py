#!/usr/bin/python3

# This program does the work of a Host at a restaurant
# It should greet a customer, find out the size of the party, and
# let the customer know if a table is available,
# otherwise, the customer should be added to a waiting list

# Original Table status -- DO NOT CHANGE!
table0 = {"max":4,"status":"occupied"}
table1 = {"max":4,"status":"occupied"}
table2 = {"max":2,"status":"occupied"}
table3 = {"max":4,"status":"occupied"}
table4 = {"max":2,"status":"occupied"}
table5 = {"max":4,"status":"occupied"}
table6 = {"max":4,"status":"occupied"}
table7 = {"max":2,"status":"occupied"}
table8 = {"max":2,"status":"occupied"}
table9 = {"max":2,"status":"available"}

# This Dictionary will keep track of waiting patrons
wait = {}

# Ask the user how many are in their party
size = input("Akwaba! How many people are in your party? ")
size = int(size)

# Check if this party will fit with the table 9 availability
# If yes - let them know they will be seated
# If no - let them know how long they must wait

if size == table9["max"]:
	print("Right this way. You will be seated at table 9.")
elif size == table9["max"]-1:
	print("Right this way. You will be seated at table 9.")
	#Could we have made the above statements better???
else:
	##MODIFY THIS CODE!!!
	# Only add party to the wait list if that name is not already on it.
	w = input("You will need to wait for a table. What is your name? ")
	wait[w] = size
	number_waiting = len(wait.keys())
	print("Approximate wait time is ",5*number_waiting, " minutes.")
