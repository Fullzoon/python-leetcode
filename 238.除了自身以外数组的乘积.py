'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''

# 方法1: 使用除法, 0的情况单独处理
def productExceptSelf1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    product = 1
    zero_list = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_list.append(i)
        else:
            product *= nums[i]

    answer = []
    for num in nums:
        if len(zero_list) > 1:
            answer.append(0)
        elif len(zero_list) == 1:
            if num == 0:
                answer.append(product)
            else:
                answer.append(0)
        else:
            answer.append(product*pow(num,-1))

    return answer


# 方法2: 先遍历计算左侧和右侧的乘积,再把他们乘到一起
def productExceptSelf2(nums):
    left_list = [1]
    right_list = [1]
    length = len(nums)
    i = 0
    while i < length-1:
        left_list.append(left_list[-1] * nums[i])
        right_list.insert(0, right_list[0] * nums[length-1-i])
        i += 1
    answer = []
    print(left_list)
    print(right_list)
    for n in range(length):
        answer.append(left_list[n]*right_list[n])
    return answer




nums1 = [-1,1,0,-3,3]

print(productExceptSelf2(nums1))