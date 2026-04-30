'''
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
'''


def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    wordList = [[]]
    wordLenList = [0]
    for word in words:
        if wordLenList[-1] + len(word) + len(wordList[-1]) <= maxWidth:
            wordList[-1].append(word)
            wordLenList[-1] += len(word)
        else:
            wordList.append([word])
            wordLenList.append(len(word))

    resultList = []
    for i in range(len(wordList) - 1):
        w = ''
        lineLen = len(wordList[i])
        if lineLen <= 1:
            w += wordList[i][0] + ''.ljust(maxWidth - len(wordList[i][0]), ' ')
            resultList.append(w)
        else:
            cycleNum = int((maxWidth - wordLenList[i]) / (lineLen - 1))
            endNum = (maxWidth - wordLenList[i]) % (lineLen - 1)
            print(cycleNum, endNum)
            for j in range(lineLen):
                if j == lineLen-1:
                    w += wordList[i][j]
                else:
                    w += wordList[i][j] + ''.ljust(cycleNum, ' ')
                    if j < endNum:
                        w += ' '
            resultList.append(w)

    lastLineStr = ' '.join(wordList[-1])
    resultList.append(lastLineStr + ''.ljust(maxWidth - len(lastLineStr), ' '))

    return resultList

words1 = ["This", "is", "an", "example", "of", "text", "justification.", 'justification', 'justification']
words2 = ['justification', 'justification', 'justification']

print(fullJustify(words1, 16))

