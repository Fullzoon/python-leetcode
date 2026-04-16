''' 80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''

# 耗时太久，跑通所有用例用时 8000ms+
def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 1
    while n < len(nums)-1:
        if nums[n] == nums[n-1] and nums[n] == nums[n+1]:
            del nums[n]
            n -= n
        n += 1

    return len(nums)

# 耗时久, 跑通所有用例耗时 8000ms+
def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) > 2:
        startIndex = 0
        startNum = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == startNum:
                i += 1
                if i == len(nums):
                    print(i)
                    nums[startIndex + 2:i] = []
            else:
                if i - startIndex > 2:
                    nums[startIndex+2:i] = []
                    i = i - (startIndex + 2)
                    startIndex = i
                    startNum = nums[i]
                else:
                    startIndex = i
                    startNum = nums[i]
                    i += 1
        return len(nums)
    else: return len(nums)

def removeDuplicates3(nums):
    length = len(nums)
    if length < 3: return length
    else:
        i = 2
        while i < length:
            if nums[i] == nums[i-2]:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return i


nums1 = [0,0,1,1,1,1,2,3,3]
nums2 = [1,1,1]

print(removeDuplicates3(nums1))
