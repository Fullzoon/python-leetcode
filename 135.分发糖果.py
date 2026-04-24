'''
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子中，评分更高的那个会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
'''

# 方法1: 正着算一遍,反着算一遍, 再逐位对比, 数字大的就是对的
def candy1(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    arr1 = [1]
    length = len(ratings)
    for index in range(1, length):
        if ratings[index] > ratings[index - 1]:
            arr1.append(arr1[index - 1] + 1)
        elif ratings[index] == ratings[index - 1]:
            arr1.append(1)
        else:
            if arr1[index - 1] == 1:
                arr1[index - 1] += 1
            arr1.append(1)

    print(arr1)
    arr2 = [1]
    ratings.reverse()
    for index in range(1, length):
        if ratings[index] > ratings[index - 1]:
            arr2.append(arr2[index - 1] + 1)
        elif ratings[index] == ratings[index - 1]:
            arr2.append(1)
        else:
            if arr2[index - 1] == 1:
                arr2[index - 1] += 1
            arr2.append(1)
    print(arr2)
    arr2.reverse()
    for index in range(length):
        if arr2[index] > arr1[index]:
            arr1[index] = arr2[index]

    return sum(arr1)

# 方法2: 正面过一遍,反面过一遍,确保数字没问题
def candy2(ratings):
    arr = [1]
    length = len(ratings)
    for index in range(1, length):
        if ratings[index] > ratings[index - 1]:
            arr.append(arr[index - 1] + 1)
        else:
            arr.append(1)

    print(arr)
    if arr[length-1] == 0: arr[length-1] = 1
    for index in range(1, length):
        if ratings[length - 1 - index] > ratings[length - index]:
            num = arr[length - index] + 1
            if num > arr[length - 1 - index]:
                arr[length - 1 - index] = num

    print(arr)
    return sum(arr)


ratings1 = [1,2,2]              # 4
ratings2 = [1,0,2]              # 5
ratings3 = [1,3,2,2,1]          # 7
ratings4 = [1,2,87,87,87,2,1]   # 13
ratings5 = [7,8,9,9,9,9,8,7,6]  # 18

print(candy2(ratings2))

