#!/usr/bin/env python

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
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

finalSum = sum([x for x in xrange(2000000) if is_prime(x)])

print 'The sum of all the primes below two million', finalSum #142913828922

