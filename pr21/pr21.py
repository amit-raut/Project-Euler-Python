#!/usr/bin/env python

'''
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b 
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

amicableNumList =[]
def sum_of_divisors(n):
	summ = 0
	for i in xrange(1, n):
		if not n % i:
			summ += i
	return summ

for num in xrange(1, 10000):
	if sum_of_divisors(num) != sum_of_divisors(sum_of_divisors(num)) and \
	sum_of_divisors(num) == sum_of_divisors(sum_of_divisors(sum_of_divisors(num))):
		amicableNumList.append(sum_of_divisors(num))

print 'The sum of all the amicable numbers under 10000 is %d.' % sum(set(amicableNumList)) #31626

