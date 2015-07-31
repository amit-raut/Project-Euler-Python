#!/usr/bin/env python

'''
The prime 41 can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that 
adds to a prime contains 21 terms and is equal to 953.

Which prime below one-million,can be written as the sum of the most consecutive primes?
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

primes = [num for num in xrange(10000) if is_prime(num)]
finalSum = 0
count = 0
finalList = []

for prime in primes[3:]:
	finalSum += prime

	if finalSum < 1000000 and is_prime(finalSum):
		finalList.append(finalSum)

print 'The prime below one-million,can be written as the sum \
of the most consecutive primes is %d.' % finalList[-1] #997651
		


