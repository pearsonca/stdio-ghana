#!/usr/bin/python3
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Dane's Solution
'''
# Recursive function
# Find prime factors of all numbers that are factors
# Append these to a list of primes, then take the max of this list
import math

def genPrimeList(num):
	if num in (1,2,3): return [num]
	primeList = []
	upto = math.floor(math.sqrt(num))
	track = 2
	if not num % track:
		primeList += genPrimeList(num/track)
	track +=1
	while track <= upto:
		if not num % track:
			primeList += genPrimeList(num/track)
			primeList += genPrimeList(track)
		track +=2
	if not primeList: primeList += [num]
	return primeList

number = 600851475143

large = max(genPrimeList(number))

print("Largest prime factor of %d is %d\n" %  (number, large))
