#!/usr/bin/env python

"""
The number  197  is called a circular prime because all rotations of the digits: 197  971  and 719  are themselves prime.

There are thirteen such primes below 100: 2  3  5  7  11  13  17  31  37  71  73  79  and 97.

How many circular primes are there below one million?
"""

from itertools import permutations
import math

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

def is_cyclic_prime(n):
	for index in xrange(1, len(str(n))):
		if not is_prime(int(str(n)[index:] + str(n)[:index])):
			return False
	return True

count = 0
for num in xrange(2, 1000000):
	if is_prime(num):
		if is_cyclic_prime(num):
			count += 1

print "Total number of circular primes below one million is %d" % count #55
