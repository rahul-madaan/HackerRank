def findMedianSortedArrays(nums1, nums2) -> float:
    nums = []
    length = len(nums1) + len(nums2)
    for x in range(len(nums1) + len(nums2)):
        if len(nums1) == 0:
            nums.extend(nums2)
            break
        elif len(nums2) == 0:
            nums.extend(nums1)
            break
        else:
            if nums1[0] <= nums2[0]:
                nums.append(nums1[0])
                nums1.remove(nums1[0])
            elif nums2[0] < nums1[0]:
                nums.append(nums2[0])
                nums2.remove(nums2[0])
    print(nums)
    print(length)
    if length%2 == 1:
        medianIndex = int(length/2)+1
        median = nums[medianIndex-1]
        print(median)
    else:
        medianIndex1 = int(length/2)
        medianIndex2 = int(length/2)+1
        median = (nums[medianIndex1-1] + nums[medianIndex2-1])/2
        print(median)


findMedianSortedArrays([1, 3, 5, 8, 10], [2, 4,4,4,5, 6, 7, 9, 11])
