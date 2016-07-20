#!/usr/bin/env python

'''
What is the 10001st prime number?
'''
import math
count = 0

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

for num in xrange(1000000):
	if is_prime(num):
		count += 1
	if count == 10001:
		print 'The 10001st prime number is', num #104743
		break

