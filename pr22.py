#!/usr/bin/env python

'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names,  
begin by sorting it into alphabetical order. Then working out 
the alphabetical value for each name, multiply this value by 
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

from urllib2 import urlopen

fileContent = urlopen('https://projecteuler.net/project/resources/p022_names.txt')
for line in fileContent:
	sortedNamesArray = sorted(line.split(','), key = str.upper)

summ = nameScore = 0

for name in sortedNamesArray:
	for ch in name:
		if ch != '"':
			summ += (ord(ch) - 64)
	nameScore += summ * (sortedNamesArray.index(name) + 1)
	summ = 0
print 'The total of all the name scores in the file is %d.' % nameScore # 871198282