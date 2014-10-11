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

# Save to pickle file
import pickle, string
pickle.dump(guilty, open( "plagarismRaw.pkl", "wb" ) )

# Write results to output file
outfile = open("plagarismRaw.csv","w")
outfile.writelines("SEARCH_WORDS\tTOP_RESULT\n")
for content,value in guilty.iteritems():
  # Filter for non ascii characters
  result = filter(lambda x: x in string.printable, " ".join(value).encode("utf-8")).replace("\n","")
  outfile.writelines(content + "\t" + result + "\n")
outfile.close()

# Now let's count the number of results with gogglesoptional to estimate the number of plagarized
import re
count = 0
expression = re.compile("goggles")
outfile = open("plagarism.csv","w")
outfile.writelines("SEARCH_WORDS\tTOP_RESULT\n")
for content,value in guilty.iteritems():
  result = filter(lambda x: x in string.printable, " ".join(value).encode("utf-8")).replace("\n","")
  match = expression.search(result)
  if not match:
    count = count + 1
    outfile.writelines(content + "\t" + result + "\n")
outfile.close()

print "Found a total of " + str(count) + " plagarized sections!"
