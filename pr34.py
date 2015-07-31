#!/usr/bin/env python

'''145 is a curious number  as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

finalSum = digitFactorialSum = 0
for num in xrange(3, 100000):
	for digit in str(num):
		digitFactorialSum += math.factorial(int(digit))
	if digitFactorialSum == num:
		# print num
		finalSum += num
	digitFactorialSum = 0

print "The sum of all numbers which are equal to the sum of \
the factorial of their digits is %d." % finalSum #40730