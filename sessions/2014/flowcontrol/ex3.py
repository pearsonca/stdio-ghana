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
table_list = [table0,table1,table2,table3,table4,table5,table6,table7,table8,table9]

# This Dictionary will keep track of waiting patrons
wait = {}

# Ask the user how many are in their party
size = input("\nAkwaba! How many people are in your party? ")

# Handle the exception of a user entering a non-number
#YOUR CODE HERE!!!
size = int(size)

# Check if this party will fit with the table 9 availability
# If yes - let them know they will be seated
# If no - let them know how long they must wait

if (table9["max"] - size) in (0,1):
	print("Right this way. You will be seated at table 9.")
elif size < 1 or size > max([sz["max"] for sz in table_list]):
	print("I'm sorry, our tables do not hold parties of that size.")
else:
	# Only add party to the wait list if that name is not already on it.
	w = input("You will need to wait for a table. What is your name? ")
	if w not in wait.keys():
		wait[w] = size
		number_waiting = len(wait.keys())
		print("Approximate wait time is ",5*number_waiting, " minutes.")
	else:
		print("I'm sorry, we can't serve you tonight. There is already a customer by that name.")

