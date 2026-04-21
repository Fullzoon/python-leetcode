'''
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
'''
# 题目比较抽象，大概意思：数组中有h个不小于h的值，求最大的h

# 方法1 从头到尾逐个判断
def hIndex1(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    h = 0
    flag = True
    while flag:
        count = 0
        for num in citations:
            if num >= h+1:
                count += 1

        if count >= h+1:
            h += 1
        else:
            flag = False

    return h

# 方法2 先排序再根据下标来确定
def hIndex2(citations):
    h = 0
    sorted_citations = sorted(citations, reverse=True)
    for n in range(0, len(sorted_citations)):
        if sorted_citations[n] >= n+1:
            h = n+1
        else:
            break
    return h



citations1 = [3,0,6,1,5]

print(hIndex2(citations1))