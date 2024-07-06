from typing import List
arr = [5, 6, 2, 7, 6, 4, 5]

def insertion_sort(nums: List[int]) -> List[int]:
    N = len(nums)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    return nums
sorted_arr = insertion_sort(arr)
print(sorted_arr)