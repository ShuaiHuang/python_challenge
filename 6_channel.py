#http://www.pythonchallenge.com/pc/def/channel.html
import os, re, zipfile
# FileBase='5_channel/'
# FileName='90052'

# FileHandle=file(FileBase+FileName+'.txt')
# FileContent=FileHandle.read()
# FileHandle.close()
# temp=re.findall(r'[0-9]+$', FileContent)

# while temp:
#     FileName=temp[0]
#     FileHandle=file(FileBase+FileName+'.txt')
#     FileContent=FileHandle.read()
#     print FileContent
#     FileHandle.close()
#     temp=re.findall(r'[0-9]+$', FileContent)

Comments=[]
ZipFileObj=zipfile.ZipFile('6_channel.zip', 'r')
Prefix='90052'
Surfix='.txt'

while True:
    FileContent=ZipFileObj.read(Prefix+Surfix)
    Temp=re.findall(r'[0-9]+$', FileContent)
    if Temp:
        Prefix=Temp[0]
        Comments.append(ZipFileObj.getinfo(Prefix+Surfix).comment)
    else:
        break

print ''.join(Comments)
#http://www.pythonchallenge.com/pc/def/hockey.html
#http://www.pythonchallenge.com/pc/def/oxygen.html