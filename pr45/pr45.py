#!/usr/bin/env python

'''
Triangle pentagonal and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1,3,6,10,15,...
Pentagonal	 	Pn=n(3n-1)/2	 	1,5,12,22,35,...
Hexagonal	 	Hn=n(2n-1)	 	1,6,15,28,45,...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

# Set of hexagonal numbers is subset of triangular numbers

pentagonalNumList = set()
hexagonalNumList =set()

for n in xrange(1, 100000):
	if n * (3 * n - 1) / 2 > 40755:
		pentagonalNumList.add( n * (3 * n - 1) / 2)
	if n * (2 * n - 1) > 40755:
		hexagonalNumList.add( n * (2 * n - 1))

print 'The next triangle number that is also pentagonal and hexagonal is %d.'\
% list(hexagonalNumList.intersection(pentagonalNumList))[0] #1533776805

