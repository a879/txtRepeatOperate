# fileUrl = 'C:/Users/knowto/Downloads/cdk.txt'

fileUrl = str(input('输入文件路径'))
oldWord = input('输入需要修改的内容（文字和符号）')
newWord = input('输入新的内容')

file1 = open(fileUrl, mode='r+', encoding="utf-8")
file1.writelines('\n\n')
# sha1.txt
d = []
for w in file1.readlines():
    d.append(w)

for s in d:
    s = s.replace(' ', '')
    s = s.replace(oldWord, newWord)
    file1.writelines('{content}'.format(content=s))

file1.close()