from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums2 = []
    for x in range(len(nums)):
        if nums[x - 1] != nums[x]:
            nums2.append(nums[x])

    nums = nums2
    print(nums)
    return len(nums)




x = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(x))