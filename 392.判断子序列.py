'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
'''


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    sLen = len(s)
    tLen = len(t)
    if sLen > tLen:
        return False
    elif sLen == tLen:
        return s == t
    else:
        if sLen == 0:
            return True
        else:
            index = 0
            for ss in s:
                print(ss)
                flag = True
                while flag:
                    if index < tLen:
                        if ss == t[index]:
                            flag = False
                    else:
                        flag = False
                    index += 1

            if index > tLen: return False
            else: return True

s1 = "ade"
s2 = 'aa'
t1 = "abcde"


print(isSubsequence(s1, t1))
print(isSubsequence(s2, t1))

