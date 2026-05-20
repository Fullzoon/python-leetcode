'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''

# 这种办法超时了
def maxArea1(height):
    """
    :type height: List[int]
    :rtype: int
    """
    length = len(height)
    x = 0
    y = length - 1

    max_area = 0
    max_x = 0
    max_y = 0
    while x < length:
        if height[x] > max_x:
            max_x = height[x]
            while y > 0 and y > x:
                if height[y] > max_y:
                    max_y = height[y]
                    area = (y - x) * min(height[x], height[y])
                    if area > max_area: max_area = area
                y -= 1
        print(x)
        x += 1
        y = length - 1
        max_y = 0
    return max_area


def maxArea2(height):
    x = 0
    y = len(height) - 1
    max_area = 0
    while x != y:
        area = (y - x) * min(height[x], height[y])
        if area > max_area:
            max_area = area
        if height[x] > height[y]:
            y -= 1
        elif height[y] > height[x]:
            x += 1
        else:
            x += 1
    return max_area


height1 = [1,8,6,2,5,4,8,3,7]

print(maxArea2(height1))
