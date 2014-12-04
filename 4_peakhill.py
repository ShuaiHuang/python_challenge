#http://www.pythonchallenge.com/pc/def/peak.html
import pickle

FileHandle=open('4_banner.p')
# FileContent=FileHandle.read()

# print FileContent
DecodedContent=pickle.load(FileHandle)
# print DecodedContent
for CurrentList in DecodedContent:
    print(''.join(t[0]*t[1] for t in CurrentList))
FileHandle.close()

#http://www.pythonchallenge.com/pc/def/channel.html