''' 26.删除有序数组中的重复项
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
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