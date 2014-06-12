#!/usr/bin/python3
import sys

# This program does the work of a Host at a restaurant
# It should greet a customer, find out the size of the party, and
# let the customer know if a table is available,
# otherwise, the customer should be added to a waiting list

# Original Table status -- DO NOT CHANGE!
tables = [None for r in range(0,9)]   # List of tables in the restaurant
tables[0] = {"max":4,"status":"occupied","number":0}
tables[1] = {"max":4,"status":"occupied","number":1}
tables[2] = {"max":2,"status":"occupied","number":2}
tables[3] = {"max":4,"status":"occupied","number":3}
tables[4] = {"max":2,"status":"available""number":4}
tables[5] = {"max":4,"status":"occupied","number":5}
tables[6] = {"max":4,"status":"available","number":6}
tables[7] = {"max":2,"status":"occupied","number":7}
tables[8] = {"max":2,"status":"occupied","number":8}
tables[9] = {"max":2,"status":"occupied","number":9}

# Function to check table availability.
def CheckTables():
	avail = []
	for place in tables:
		if place["max"] - size in (0,1) and place["status"] is "occupied":
			avail.append(place["number"])
	return avail

# This Dictionary will keep track of waiting patrons
wait = []

# Create a loop which allows multiple visitors to request tables
# A party size of zero should indicate an empty line
# *Interesting addition: Have a table randomly made available each iteration*

while 1;
	# Ask the user how many are in their party
	size = input("\nAkwaba! How many people are in your party? ")
	
	size = int(size)
	
	# Check if this party will fit with any table availability
	# Discern availability of tables inside a function
	avail_tables = CheckTables
			
	# If yes - let them know they will be seated
	# If no - let them know how long they must wait
	
	if avail_tables:
		your_table = avail_tables.pop()
		print("Right this way. You will be seated at table %d." % your_table)
		tables[your_table]["status"] = "occupied"
	elif size <= 0 or size > max([sz["max"] for sz in tables]):
		print("I'm sorry, our tables do not hold parties of that size.")
	elif size == 0:
		print("\nI see the line is now empty.  We are closing for the evening.\n")
		break
	else:
		# Only add party to the wait list if that name is not already on it.
		w = input("You will need to wait for a table. What is your name? ")
		try: eval(w)
		except NameError: None
	
		if w not in wait.keys():
			wait[w] = size
			number_waiting = len(wait.keys())
			print("Approximate wait time is ",5*number_waiting, " minutes.")
		else:
			print("I'm sorry, we can't serve you tonight. There is already a customer by that name.")
	
