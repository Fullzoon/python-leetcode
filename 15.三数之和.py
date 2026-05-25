'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    length = len(nums)
    ansList = []
    nums.sort()
    if nums[0] > 0:
        return []
    elif length == 3 and nums[0] + nums[1] + nums[2] == 0:
        return [[nums[0], nums[1], nums[2]]]
    i = 0
    while i < length - 2 and nums[i] <= 0:
        l = i + 1
        r = length - 1
        while r > l and (i == 0 or nums[i] != nums[i-1]):
            count = nums[i] + nums[l] + nums[r]
            if count == 0:
                if nums[l] == nums[l + 1] and l+1 < r:
                    l += 1
                elif nums[r] == nums[r - 1] and r - 1 > l:
                    r -= 1
                else:
                    ansList.append([nums[i], nums[l], nums[r]])
                    r -= 1
            elif count < 0:
                l += 1
            elif count > 0:
                r -= 1

        i += 1

    return ansList



nums1 = [-1,0,1,2,-1,-4]
nums2 = [-1, -1, -1, -1, -1, -1, -1, 2]
nums3 = [0,0,0,0,0]
print(threeSum(nums3))

