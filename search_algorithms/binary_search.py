#classic search algorithm, do the split in the middle of a sorted list and move left or right depending on if the target is larger or smaller than the halfed number
def binary_search_vanilla(target, arr):
    if len(arr) < 1:
        return
    half = len(arr) // 2
    if arr[half] == target:
        return half
    else:
        if arr[half] > target:
            return binary_search_vanilla(target, arr[:half]) 
        else:
            return binary_search_vanilla(target, arr[half:]) 

print(binary_search_vanilla(1, [1,2,4,5,6,7,8]))

#pointer method
def binary_search_pointers(array, v):
    low = 0
    high = len(array)
    while low <= high:
        mid = (low+high) // 2
        if array[mid] == v:
            return mid
        if array[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(binary_search_pointers([1,2,3,4,5,6,7,8,9],3))
