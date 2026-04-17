''' 169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    obj = {}
    for num in nums:
        if num not in obj:
            obj[num] = 1
        else:
            obj[num] += 1
        if obj[num] > len(nums)/2:
            return num


nums1 = [2,2,1,1,1,2,2]

print(majorityElement(nums1))