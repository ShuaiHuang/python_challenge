# http://www.pythonchallenge.com/pc/def/ocr.html
FileHandle=file('2_data')
MessString=FileHandle.read()
FileHandle.close()
print filter(lambda x: ord(x) in range(ord('a'), ord('z')+1), MessString)
# http://www.pythonchallenge.com/pc/def/equality.html