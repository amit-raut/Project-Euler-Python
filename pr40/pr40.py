#!/usr/bin/env python

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

digitsString = ''
for i in xrange(1, 1000001):
	digitsString += str(i)

fianlProduct = int(digitsString[0]) * int(digitsString[9])* int(digitsString[99]) * int(digitsString[999]) * int(digitsString[9999]) * int(digitsString[99999]) * int(digitsString[999999])

print 'The desired product is %d.' % fianlProduct #210