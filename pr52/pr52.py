#!/usr/bin/env python

'''
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
'''

def digitsInNumber(n):
	return sorted([digit for digit in str(n)])

for num in xrange(100000, 999999):
	flag = False
	for i in [digitsInNumber(x) for x in [num * 2, num * 3, num * 4, num * 5, num * 6]]:
		if digitsInNumber(num) != i:
			flag = False
			break
		else:
			flag = True
	if flag:
		print 'The smallest positive integer, x, such that 2x, 3x, 4x, 5x, \
and 6x, contain the same digits is %d.' % num #142857
		break

