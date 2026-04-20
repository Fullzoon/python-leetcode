'''
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
'''


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    step = nums[0]
    length = len(nums)
    if length == 1: return True
    elif step == 0: return False

    for i in range(1, length):
        step -= 1
        if step > length-1-i or i == length-1:
            return True
        if step == 0 and nums[i] == 0:
            return False
        if nums[i] > step:
            step = nums[i]


nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

print(canJump(nums2))