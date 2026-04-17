'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    kn = k % length
    if length == 1 or kn == 0:
        return nums
    else:
        nums[0:0] = nums[length - kn:]
        nums[length:] = []

    print(nums)

nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)
