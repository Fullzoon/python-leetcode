'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：
'''

def jump1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    flag = True
    count = 0
    length = len(nums) - 1
    if length == 0: return 0
    while flag:
        for i in range(length):
            print(i)
            if nums[i] >= length - i:
                count += 1
                if i == 0:
                    flag = False
                else:
                    length = i
                break

        print('-----')

    return count

def jump2(nums):
    length = len(nums)
    cur_end = 0
    far_end = 0
    ans = 0
    for i in range(length - 1):
        far_end = max(far_end, i + nums[i])
        if i == cur_end:
            ans += 1
            cur_end = far_end
    return ans



nums1 = [2,3,1,1,4]
nums2 = [2,3,0,1,4]
nums3 = [0]

print(jump2(nums1))
