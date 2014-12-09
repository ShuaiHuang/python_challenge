#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pythonchallenge.com/pc/return/evil.html

import Image, ImageEnhance

# Img=Image.open('12_evil1.jpg')
# print Img.format, Img.size, Img.mode

# http://www.pythonchallenge.com/pc/return/evil2.jpg
# http://www.pythonchallenge.com/pc/return/evil3.jpg
# http://www.pythonchallenge.com/pc/return/evil4.jpg
FileHandle=open('12_evil2.gfx', 'rb')
FileContent=FileHandle.read()
for Counter in range(5):
    File=open('evil_%d.jpg'% Counter, 'wb')
    File.write(FileContent[Counter::5])
    File.close()

FileHandle.close()
# http://www.pythonchallenge.com/pc/return/disproportional.html