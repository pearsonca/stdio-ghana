#!/usr/bin/python3
#This program divides two numbers
# The function below calculates and returns the division result
def div(x,y,z):
	q = x/y
	return q
# Main portion of program to set up the problem
a = int(input("Enter the first operand: "))
b = int(input("Enter the second operand: "))
c = div(a,b)
print("\nYour answer is %d\n" % c)
