#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pythonchallenge.com/pc/return/bull.html
# Length_a=[1, 2, 2, 4, 6]
# for Counter in range(5,31):
#     print Length_a[-1], Length_a[-2]
#     Length_a.append(Length_a[-1]+Length_a[-2])
# print Length_a[30], len(Length_a)

import re

def Sequence(Str):
    return ''.join([str(len(m.group(0)))+m.group(1) for m in re.finditer(r'(\d)\1*', Str)])

Str='1'
for Counter in range(30):
    Str=Sequence(Str)

print len(Str)
# http://www.pythonchallenge.com/pc/return/5808.html