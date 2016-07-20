#!/usr/bin/env python

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

summ = result = 0

for num in xrange(2, 1000000):
	for digit in str(num):
		summ += int(digit) ** 5
	if summ == num:
		result += num
	summ = 0

print 'The sum of all the numbers that can be written as the \
sum of fifth powers of their digits is %d.' % result # 443839
