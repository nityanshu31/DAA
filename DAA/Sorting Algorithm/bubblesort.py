from typing import List

arr = [5, 6, 2, 7, 6, 4, 5]

def bubble_sort(arr: List[int]) -> List[int]:
    N = len(arr)
    for i in range(N):
        swapped = False
        for j in range(0, N - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_arr = bubble_sort(arr)
print(sorted_arr)
