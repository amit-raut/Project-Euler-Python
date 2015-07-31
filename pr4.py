#!/usr/bin/env python

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
largestPalindrome = 1

for i in xrange(999, 800, -1):
	for j in xrange(999, 800, -1):
		if str(i * j) == str(i * j)[::-1]:
			largestPalindrome = max(largestPalindrome, i * j)

print 'The largest palindrome made from the product of two 3-digit numbers is', largestPalindrome #906609
