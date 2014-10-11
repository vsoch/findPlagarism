# -*- coding: utf-8 -*-

# Credit for this goes to: http://www.zombrec.be/plagiarism.py

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Given a list of words and a number n, return a list
# of n-grams.
def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

# Query Google if a given string, preferably a sentence (min. 8 words?),
# is plagiarized (copied literally) from an available web source.
# The 'encode' flag can be used if the given string is a Unicode (UTF-8)
# string.
def GPlag(text,encode=False):
    import urllib, urllib2, simplejson
    if encode == True:
        text = text.encode('utf-8')
    query = urllib.quote_plus(text)
    base_url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
    url = base_url + '%22' + query + '%22'
    print url
    request = urllib2.Request(url,None,{'Referer':'http://www.example.com'})
    response = urllib2.urlopen(request)
    results = simplejson.load(response)
    output = []
    if results['responseData']['results'] != []:
      firstMatch = results['responseData']['results'][0]
      output.append(firstMatch['title'])
      output.append(firstMatch['url'])
      output.append(firstMatch['content'])
    return output

# Use the GPlag() function to scrutinize a file for
# plagiarism
def GPlagFile(file,n=9):
    import codecs
    import sys
    t=codecs.open(file,'r','utf-8').read()
    ngrams = getNGrams(stripNonAlphaNum(t),n)
    n = [' '.join(d) for d in ngrams]
    found = []
    for s in n:
        outcome = GPlag(s,encode=True)
        if outcome != []:
            print s
            sys.stdout.flush()
