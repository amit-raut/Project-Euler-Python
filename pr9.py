#!/usr/bin/env python
import math

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for i in xrange(1, 999):
	for j in xrange(1, 1000 - i):
		if int(math.sqrt(i * i + j * j)) ** 2 == (i * i + j * j) and i + j + int(math.sqrt(i * i + j * j)) == 1000 and i < j:
			print 'Product of Pythagorean triplet with 1000 as their sum is', i * j * int(math.sqrt(i * i + j * j)) #31875000
			break

