#classic search algorithm, do the split in the middle of a sorted list and move left or right depending on if the target is larger or smaller than the halfed number
def binary_search_vanilla(target, arr):
    if len(arr) < 1:
        return
    half = len(arr) // 2
    if arr[half] == target:
        return True
    else:
        if arr[half] > target:
            return binary_search_vanilla(target, arr[:half]) or False
        else:
            return binary_search_vanilla(target, arr[half:]) or False

print(binary_search_vanilla(1, [1,2,4,5,6,7,8]))

#pointer method
def binary_search_pointers():
    return