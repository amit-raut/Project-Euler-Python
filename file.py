#!/usr/bin/env python

from urllib2 import urlopen
import csv 


file_url = 'https://projecteuler.net/project/resources/p042_words.txt'

f = urlopen(file_url)

print f.read().replace('"', '').split(',')

