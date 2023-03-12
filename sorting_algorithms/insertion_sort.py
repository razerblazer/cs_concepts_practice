#this sort works well for small array sizes

"""
algorithm works by going to each element in a list and "inserting" it into where it actually belongs.
Ex: [2,3,4,1]
assuming we are on the last index(for the value of 1), 1 would be inserted into the front of the list where it belongs after many swaps
"""
def insertion_sort(arr):
    for num in range(1, len(arr)):
        current_num, number = num, arr[num]
        while num > 0 and arr[current_num] < arr[num-1]:
            arr[num-1], arr[current_num] = arr[current_num], arr[num-1]
            num -= 1
            current_num -= 1
    return arr

print(insertion_sort([4,3,2,1]))