#!/usr/bin/env python

""" The fraction 49/98 is a curious fraction  as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8  which is correct  is obtained by cancelling the 9s.

We shall consider fractions like  30/50 = 3/5  to be trivial examples.

There are exactly four non-trivial examples of this type of fraction  less than one in value  and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms find the value of the denominator.

"""

print "The required pair of numbers are...."
numerator = denominator = 1
for i in xrange(11, 100):
	for j in xrange(11, 100):
		if i % 10 == j / 10 and j % 10 and float(i / 10) / float(j % 10) == float(i) / float(j) and i != j:
			numerator *= i
			denominator *= j

print "The product of numbers is %f" % (numerator/ float(denominator)) # 0.01 = 1/100