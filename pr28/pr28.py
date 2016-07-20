#!/usr/bin/env python

'''
Starting with the number 1 and moving to the right in 
a clockwise direction a 5 by 5 spiral is formed as follows:

[21]  22  23  24 [25]
 20  [7]  8  [9]  10
 19   6  [1]  2   11
 18  [5]  4  [3]  12
[17]  16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals 
in a 1001 by 1001 spiral formed in the same way?
'''

num, increment = 1, 2
summ = result = 0
for i in xrange(1002002 // 4): # 1001x1001 grid contains 1002001 elements hence bound 1002002
	for j in xrange(4):
		if num >= 1002002:
			break
		result += num
		num += increment
	
	increment += 2

print 'The sum of the numbers on the diagonals \
in a 1001 by 1001 spiral formed by the about way is %d' % result # 669171001
