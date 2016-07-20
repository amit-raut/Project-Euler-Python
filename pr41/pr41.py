#!/usr/bin/env python

'''
We shall say that an n-digit number is pandigital if it 
makes use of all the digits 1 to n exactly once. 
For example,2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
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


maxPrime = 0
for i in xrange(1, 10):
	for num in permutations(str('1234567890')[:i]):
		if is_prime(int(''.join(num))):
			maxPrime = max(maxPrime,int(''.join(num)))

print 'The n-digit pandigital prime number is',maxPrime #7652413
