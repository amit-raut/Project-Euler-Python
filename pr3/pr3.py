#!/usr/bin/env python

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

n = 600851475143
i = 1
maxProduct = 1
while i * i < n:
	if not n % i:
		n = n // i
		if is_prime(i):
			maxProduct = max(maxProduct, i)
		if is_prime(n):
			maxProduct = max(maxProduct, n)
	i += 1

print 'The largest prime factor of the number 600851475143 is', maxProduct