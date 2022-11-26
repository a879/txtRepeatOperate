# 通过io打开目标路径的文件，遍历文件内容，添加到列表中
# io操作 r+ 不能修改为a+, 无法处理
# io操作read无法同时执行两次
# fileUrl = 'C:/Users/knowto/Downloads/cdk.txt'

fileUrl = str(input('输入文件路径'))
# isRemake = int(input('是否修改原文件： 1不修改，新建文件，2原文基础上换行添加修改后的内容'))

# if isRemake == 1:
#     mode = 'r+'
# else:
#     mode = 'w+'

file1 = open(fileUrl, mode='r+', encoding="utf-8")
file1.writelines('\n\n')
# 使用try with， 防止代码异常，close方法没有执行
try:
    while True:
        oldWord = input('输入需要修改的内容（文字和符号）')

        if oldWord:
            newWord = input('输入新的内容')
            # sha1.txt
            d = []
            for w in file1.readlines():
                d.append(w)

            for s in d:
                s = s.replace(' ', '')
                s = s.replace(oldWord, newWord)
                file1.writelines('{content}'.format(content=s))

            continue
        else:
            print('jieshu')
            break
finally:
    file1.close()
