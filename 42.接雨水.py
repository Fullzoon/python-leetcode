'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    height1 = 0
    height1index = -1
    height2 = 0
    count = 0
    length = len(height)
    for i in range(length):
        if height[i] >= height1:
            height1 = height[i]
            height1index = i

    if height1 == 0: return 0

    for i in range(height1index):
        if height[i] > height2:
            height2 = height[i]
        else:
            count += height2 - height[i]

    height2 = 0
    for i in range(length - 1 - height1index):
        if height[length - 1 - i] > height2:
            height2 = height[length - 1 - i]
        else:
            count += height2 - height[length - 1 - i]

    return count

height_arr1 = [0,1,0,2,1,0,1,3,2,1,2,1]     # 6
height_arr2 = [4,2,0,3,2,5]                 # 9


print(trap(height_arr2))