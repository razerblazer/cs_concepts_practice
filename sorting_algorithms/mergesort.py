def merge_sort(array):
    if len(array) <= 1:
        return array
    bananasplit = len(array)//2
    left = array[:bananasplit]
    right = array[bananasplit:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    finalresult = []
    
    l = r = numofiterations = 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            finalresult.append(left[l])
            l += 1
        else:
            finalresult.append(right[r])
            r += 1
    if l < len(left):
        finalresult += left[l:]
    if r < len(right):
        finalresult += right[r:]
    
    return finalresult