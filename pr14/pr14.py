#!/usr/bin/env python

'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def max_Collatz_chain(n):
	count = 0
	while n > 1:
		count += 1
		if not n % 2:
			n = n // 2
		else:
			n = 3 * n + 1
	return count

maxChain = [0, 0]

for num in xrange(1000000, 1, -1):
	if maxChain[0] < max_Collatz_chain(num):
		maxChain[0] = max_Collatz_chain(num)
		maxChain[1] = num
		
print 'The %d, under million, produces longest chain of %d elements' %(maxChain[1], maxChain[0]) #837799 524


