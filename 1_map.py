# http://www.pythonchallenge.com/pc/def/map.html
import string

def Decode(RawString):
    Key=[chr(x) for x in range(ord('a'), ord('z')+1)]
    Value=Key[-2:]+Key[:-2]
    map=string.maketrans(''.join(Value), ''.join(Key))
    print RawString.translate(map)

RawString='''
g fmnc wms bgblr rpylqjyrc gr zw fylb.
 rfyrq ufyr amknsrcpq ypc dmp.
  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
 sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''
Decode(RawString)

RawString='map'
Decode(RawString)

# http://www.pythonchallenge.com/pc/def/ocr.html