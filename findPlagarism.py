#!/usr/bin/env python2

# This script will use plagarism.py to search a folder of text documents for plagarism
# Plagarism is defined as finding a string available in a web source
# This google search API is deprecated, so a pause is added to not get in trouble!

import plagarism as p
import time

# Read in articles
filey = open("articles.csv",'r').readlines()
filey.pop(0) # Get rid of header

# Here we will save the results
guilty = dict()

for f in range(0,len(filey)):
  ff = filey[f]
  print "Finding plagarism in " + str(f) + " of " + str(len(filey))
  content = ff.strip("\n").split("\t")[-1].strip('"')
  print content
  time.sleep(10)
  result = p.GPlag(content,encode=False)
  if result:
    guilty[content] = result

# TODO: Write results to output file

