#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pythonchallenge.com/pc/return/5808.html
import Image

Img=Image.open('11_cave.jpg')

OddImage=EvenImage=Image.new(Img.mode, (320, 240))

for x in range(640):
    for y in range(480):
        pixel=Img.getpixel((x, y))
        if x%2==0 and y%2==0:
            OddImage.putpixel((x/2, y/2), pixel)
        elif x%2==1 and y%2==0:
            EvenImage.putpixel(((x-1)/2, y/2), pixel)
        elif x%2==0 and y%2==1:
            EvenImage.putpixel((x/2, (y-1)/2), pixel)
        elif x%2==1 and y%2==1:
            OddImage.putpixel(((x-1)/2, (y-1)/2), pixel)

OddImage.save('11_Odd.jpg')
EvenImage.save('11_Even.jpg')

# http://www.pythonchallenge.com/pc/return/evil.html