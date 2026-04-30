'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
'''


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    strList = []
    length = len(s)
    if numRows == 1: return s
    for index in range(length):
        nLength = numRows * 2 - 2
        if index < numRows:
            strList.append(s[index])
        else:
            yu = index % nLength
            if yu < numRows:
                strList[yu] += s[index]
            else:
                strList[nLength - yu] += s[index]

    return ''.join(strList)

s1 = "PAYPALISHIRING"   # PAHNAPLSIIGYIR
numRows1 = 3

s2 = "PAYPALISHIRING"   # PINALSIGYAHRPI
numRows2 = 4

print(convert(s2, numRows2))
