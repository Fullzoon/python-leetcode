def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        del nums1[:]
        nums1.extend(nums2)
    elif n == 0: return
    else:
        del nums1[m:]
        if nums2[0] >= nums1[m-1]:
            nums1.extend(nums2)
        elif nums2[n-1] <= nums1[0]:
            nums1[0:0] = nums2
        else:
            i = 0
            flag = True
            while flag:
                if len(nums2) == 0:
                    flag = False
                elif i == len(nums1):
                    nums1.extend(nums2)
                    flag = False
                else:
                    if nums2[0] <= nums1[i]:
                        nums1.insert(i, nums2.pop(0))
                        i += 1
                    else:
                        i += 1

    print(nums1)



nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [3, 2, 1]
nums3 = [0]


merge(nums1, 3, nums2, 3)


