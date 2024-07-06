from typing import List
arr = [3, 1, 5, 4, 2]


def cyclic_sort(nums: List[int]) -> List[int]:
    N = len(nums)
    i = 0
    while i < N:
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    return nums
sorted_arr = cyclic_sort(arr)
print(sorted_arr)