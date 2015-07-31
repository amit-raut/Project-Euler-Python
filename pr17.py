#!/usr/bin/env python

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

num2wordUpTo19 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

num2wordTensPlaces = ['0', '1', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def num_to_words(n):
	if n == 1000:
		return 'One Thousand'
	elif n >= 1 and n <= 19:
		return num2wordUpTo19[n]
	elif n >= 20 and n <= 99 and not n % 10:
		return num2wordTensPlaces[n / 10]
	elif n >= 20 and n <= 99:
		return num2wordTensPlaces[n / 10] +' '+ num2wordUpTo19[n % 10]
	elif n == 100:
		return 'One Hundred'
	elif n > 100 and n <= 999:
		if n % 100 >= 1 and n % 100 <= 19:
			return num2wordUpTo19[n / 100] + ' hundred and ' + num2wordUpTo19[n % 100]
		elif n % 100 >= 20 and n % 100 <= 99 and not (n % 100) % 10:
			return num2wordUpTo19[n / 100] + ' hundred and ' + num2wordTensPlaces[(n % 100) / 10]
		elif n % 100 >= 20 and n % 100 <= 99:
			return num2wordUpTo19[n / 100] + ' hundred and ' + num2wordTensPlaces[(n % 100) / 10] + ' ' + num2wordUpTo19[(n % 100) % 10]
		else:
			return num2wordUpTo19[n / 100] + ' Hundred'
	else:
		return 'The number is either negative or above 1000'

no_of_letters = 0

for num in xrange(1, 1001):
	for ch in num_to_words(num):
		if ch != ' ':
			no_of_letters += 1

print 'Total number of letters used when 1 to 1000 are written in words is', no_of_letters #21124






