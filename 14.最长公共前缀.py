'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    s = ''
    for index in range(0, len(strs[0])):
        ss = strs[0][0:index+1]
        for item in strs:
            if not item.startswith(ss):
                return s

        s = ss

    return s

strs1 = ["flower","flow","flight"]
strs2 = ["","flight"]
strs3 = ["flower","flower","flower"]

print(longestCommonPrefix(strs3))
