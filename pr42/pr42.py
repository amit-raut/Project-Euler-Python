#!/usr/bin/env python

'''
The nth term of the sequence of triangle numbers is given by  tn = 1/2*n(n+1); so the first ten triangle numbers are:

1  3  6  10  15  21  28  36  45  55  ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example  the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...')  a 16K text file containing nearly two-thousand common English words  how many are triangle words?
'''
from urllib2 import urlopen

triangleNumberList = []
count = 0
wordList_url = 'https://projecteuler.net/project/resources/p042_words.txt'
wordList = urlopen(wordList_url).read().replace('"', '').split(',')

for n in xrange(1, 5000):
	triangleNumberList.append(n * (n + 1) // 2)

for word in wordList:
	wordValue = 0
	for char in word:
		wordValue += (ord(char) - 64)
	if wordValue in triangleNumberList:
		count += 1
	wordValue = 0

print 'The number of triangular words in given wordlist is', count #162
