'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''
from operator import length_hint


def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    lIndex = 0
    rIndex = 1
    result = 0
    count = nums[0]
    flag = True
    while flag:
        print('left: ', lIndex, ' right: ', rIndex, ' count: ', count)
        print('----')
        # 满足条件
        if count >= target:
            if result == 0:
                result = rIndex - lIndex
            elif rIndex - lIndex < result:
                result = rIndex - lIndex
                if result == 1:
                    flag = False
            lIndex += 1
            count = count - nums[lIndex-1]
        elif rIndex < len(nums):
            rIndex += 1
            count = count + nums[rIndex-1]
        else:
            flag = False

    return result

target1 = 7
nums1 = [2,3,1,2,4,3]

print(minSubArrayLen(target1, nums1))

