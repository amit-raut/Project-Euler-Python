#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself  it is possible to continuously remove digits from left to right  and remain prime at each stage: 3797  797  97  and 7. Similarly we can work from right to left: 3797  379  37  and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math

count = finalSum = 0

def is_prime(n):
	i = 3
	if n == 1:
		return False
	elif n == 2:
		return True
	elif n % 2:
		while i < math.sqrt(n) + 1:
			if not n % i:
				return False
			i += 2
		return True
	else:
		return False
		
def is_truncatable_prime(n):
	returnFlag = False
	for index in xrange(1, len(str(n))):
		if is_prime(int(str(n)[:index])) and is_prime(int(str(n)[index:])):
			returnFlag = True
		else:
			returnFlag = False
			break
	return returnFlag

for num in xrange(10, 1000000):
	if is_prime(num) and is_truncatable_prime(num):
		count += 1
		finalSum += num
		if count == 11:
			print "The sum of the only 11 truncatable prime is %d" % finalSum #748317
			break


