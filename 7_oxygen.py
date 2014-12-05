#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pythonchallenge.com/pc/def/oxygen.html
import Image, urllib2, cStringIO

Url='http://www.pythonchallenge.com/pc/def/oxygen.png'
File=urllib2.urlopen(Url)
TempImg=cStringIO.StringIO(File.read())
Img=Image.open(TempImg)

# print Img.format, Img.size, Img.mode
print ''.join([chr(Img.getpixel((i, 43))[0]) for i in xrange(0, 603, 7)])
print ''.join(chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121])
# http://www.pythonchallenge.com/pc/def/integrity.html