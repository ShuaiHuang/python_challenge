#http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib
import re

def getAddress(Head, Tail, NumberStr):
    URL='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    for Counter in range(Head, Tail):
        Content=urllib.urlopen(URL+NumberStr).read()
        print Content
        Number=re.search(r'\s[0-9]+', Content)
        NumberStr=Number.group(0)
        print Counter, NumberStr
getAddress(1, 247, '1234')
#http://www.pythonchallenge.com/pc/def/peak.html