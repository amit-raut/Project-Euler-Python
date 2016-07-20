#!/usr/bin/env python

'''
If p is the perimeter of a right angle triangle with integral length 
sides  {a, b, c}  there are exactly three solutions for p = 120.

{20, 48, 52}  {24, 45, 51}  {30, 40, 50}

For which value of p <= 1000  is the number of solutions maximised?
'''

import math
from collections import Counter

listofVerticies = []

for i in xrange(1, 999):
	for j in xrange(1, 1000 - i):
		if int(math.sqrt(i * i + j * j)) ** 2 == (i * i + j * j) and \
			i + j + int(math.sqrt(i * i + j * j)) <= 1000:
			listofVerticies.append(i + j + int(math.sqrt(i * i + j * j)))

maxCount = Counter(listofVerticies)

print 'The value with maximum solutions is %d.' % maxCount.most_common()[0][0] #840