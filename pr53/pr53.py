#!/usr/bin/env python

'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

nCr = n! / r! / (n-r)!, where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
'''
import math
count = 0

def nCr(n, r):
	return math.factorial(n) / math.factorial(r) / math.factorial(n - r)

for n in xrange(1, 101):
	for r in xrange(1, 101):
		if r <= n and nCr(n, r) > 1000000:
			count += 1

print 'There are %d values of  nCr, for 1 <= n <= 100, are greater than one-million.' % count


