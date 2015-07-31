#!/usr/bin/env python

'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sumOfSquare = summ = 0

for num in xrange(1, 101):
	sumOfSquare += num * num
	summ += num
print 'The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is', summ * summ - sumOfSquare
#25164150
