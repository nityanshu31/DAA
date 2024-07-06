def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    sortedLeft= merge_sort(nums[:mid])
    sortedRight = merge_sort(nums[mid:])
    
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merge_sort(nums)
print(sorted_nums)
