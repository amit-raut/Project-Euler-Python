#!/usr/bin/env python

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def lcm(x, y):
	return  x * y // gcd(x, y)

print 'The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is', reduce(lcm, xrange(1, 20)) #232792560
