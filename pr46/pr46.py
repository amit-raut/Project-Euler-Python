#!/usr/bin/env python

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

squares = [2 * i * i for i in xrange(1,6000)]
primes = [i for i in xrange(6000) if is_prime(i)]
oddComposite = set([i for i in xrange(2,6000) if not is_prime(i) and i % 2])

finalSet = set([prime + square for prime in primes for square in squares])


print 'The smallest odd composite that cannot be written as \
the sum of a prime and twice a square is %d.' % list(oddComposite.difference(sorted(finalSet)))[0] #5777


