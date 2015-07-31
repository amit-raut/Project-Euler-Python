#!/usr/bin/env python

'''
The arithmetic sequence,1487,4817,8147,in which each of the 
terms increases by 3330,is unusual in two ways: (i) each of 
the three terms are prime,and,(ii) each of the 4-digit numbers 
are permutations of one another.

There are no arithmetic sequences made up of three 1-,2-,or 
3-digit primes,exhibiting this property,but there is one other 
4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import math
from itertools import permutations

addingConst = 3330
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

for num in xrange(1001, 9999 - addingConst * 2):
	if is_prime(num) and is_prime(num + addingConst) and \
	is_prime(num + addingConst * 2):
		if num != 1487 and str(num + addingConst) in \
		[''.join(x) for x in permutations(str(num))] and \
		str(num + addingConst * 2) in [''.join(x) for x in permutations(str(num))]:
			print 'Expected 12-digit numbers is %s' \
				% str(num) + str(num + addingConst) + str(num + addingConst * 2) #296962999629
			break
