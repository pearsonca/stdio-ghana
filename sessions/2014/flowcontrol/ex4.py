#!/usr/bin/python3
import sys

# This program does the work of a Host at a restaurant
# It should greet a customer, find out the size of the party, and
# let the customer know if a table is available,
# otherwise, the customer should be added to a waiting list

# Original Table status -- DO NOT CHANGE!
tables = [None for r in range(10)]   # List of tables in the restaurant
tables[0] = {"max":4,"status":"occupied","number":0}
tables[1] = {"max":4,"status":"occupied","number":1}
tables[2] = {"max":2,"status":"occupied","number":2}
tables[3] = {"max":4,"status":"occupied","number":3}
tables[4] = {"max":2,"status":"available","number":4}
tables[5] = {"max":4,"status":"occupied","number":5}
tables[6] = {"max":4,"status":"available","number":6}
tables[7] = {"max":2,"status":"occupied","number":7}
tables[8] = {"max":2,"status":"occupied","number":8}
tables[9] = {"max":2,"status":"occupied","number":9}

# This Dictionary will keep track of waiting patrons
wait = {}

######################### MODIFY CODE BELOW!! ##########################
# Create a loop which allows multiple visitors to request tables
# A party size of zero should indicate an empty line
# Don't forget to indent properly!!!

# Ask the user how many are in their party
size = input("Akwaba! How many people are in your party? ")

# Handle the exception of a user entering a non-number
try: 
	size = int(size)
except ValueError:
	print("OK Joker, try again when you can enter a real number.\nGoodbye!")
	sys.exit(0)	

# Check if this party will fit with any table availability
avail_tables = []
for place in tables:
	if place["max"] - size in (0,1) and place["status"] is "available":
		avail_tables.append(place["number"])
		
# If yes - let them know they will be seated
# If no - let them know how long they must wait

if avail_tables:
	your_table = avail_tables.pop()
	print("Right this way. You will be seated at table %d." % your_table)
	tables[your_table]["status"] = "occupied"
elif size < 1 or size > max([sz["max"] for sz in tables]):
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

