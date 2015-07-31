#!/usr/bin/env python

'''
The decimal number  585 = 10010010012 (binary)  is palindromic in both bases.

Find the sum of all numbers  less than one million  which are palindromic in base 10 and base 2.

(Please note that the palindromic number  in either base  may not include leading zeros.)
'''

finalSum = 0

for num in xrange(1000000):
	if str(num) == str(num)[::-1] and str("{0:b}".format(num)) == str("{0:b}".format(num))[::-1]:
		finalSum += num

print "Sum of all numbers below one million  which are palindromic in base 10 and base 2 is %d." % finalSum #872187