#!/usr/bin/env python

'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
summ = 0

for i in str(2 ** 1000):
	summ += int(i)

print 'The sum of the digits of the number 2^1000 is', summ