# http://www.pythonchallenge.com/pc/def/equality.html
import re
FileHandle=file('3_data')
MessString=FileHandle.read()

Result=re.findall(r'[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+', MessString)
# print Result
Address=''
for letters in Result:
    # print letters
    temp=re.search(r'[A-Z]{3}[a-z]{1}[A-Z]{3}', letters)
    Address=Address+temp.group(0)[3]
print Address
#http://www.pythonchallenge.com/pc/def/linkedlist.html