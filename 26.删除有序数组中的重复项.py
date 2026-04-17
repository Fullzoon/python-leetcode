''' 26.删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。
'''

# 我的解法 效率低
def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 1
    while n < len(nums):
        if nums[n] == nums[n-1]:
            nums[n:n+1] = []
            n -= 1
        n += 1
    return len(nums)


# 0ms 解法
def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0
    for i in range(1, len(nums)):
        if nums[n] != nums[i]:
            nums[n] = nums[i]
            n += 1
    return n + 1



nums1 = [0,0,1,1,1,2,2,3,3,4]


print(removeDuplicates2(nums1))