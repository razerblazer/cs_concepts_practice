#heap sort
import math
from io import StringIO
import heapq

class heaptime:
    def __init__(self, arr=[]):
        self.heap = arr
    def visualize_heap(self, total_width=60, fill=' '):
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.heap):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        return
    
def insert_helper(arr, position):
    if position == 0:
        return
    parent = (position // 2) - 1
    if arr[position] > arr[parent]:
        arr[parent], arr[position] = arr[position], arr[parent]
    insert_helper(arr, parent)
    
    
#insert into max heap by insertion(insert elements one by one and modify heap as required) O(nlogn) done
def max_insertion(insert, arr):
    arr.append(insert)
    insert_helper(arr, len(arr)-1)
    return arr

test = [-97, -37, -91, -12, -5, -90, -64, -1, -6]
heapq.heapify(test)
#print(max_insertion(6, [97, 37, 91, 12, 5, 90, 64, 1]))
#print(test)
#o = heaptime(test)
#p = heaptime(max_insertion(6, [97, 37, 91, 12, 5, 90, 64, 1]))
#o.visualize_heap()
#p.visualize_heap()

#heapify:transform_max_heapify(go to each node, check children and modify going up)
def max_heapify_helper(arr, parent):
    left_child = (parent * 2) +1
    right_child= (parent * 2) +2
    
    if left_child > len(arr)-1 and right_child > len(arr)-1:
        return arr
    else:
        if not (right_child > len(arr)-1) and arr[right_child] > arr[left_child] and arr[right_child] > arr[parent]:
            arr[parent], arr[right_child] = arr[right_child], arr[parent]
        else:
            if arr[left_child] > arr[parent]:
                arr[parent], arr[left_child] = arr[left_child], arr[parent]
    max_heapify_helper(arr, parent+1)
    return arr
        
def transform_max_heapify(arr):
    
    for i in range(len(arr)-1, -1, -1):
        arr = max_heapify_helper(arr, i)
    return arr
#print(transform_max_heapify([10, 20, 15, 12, 40, 25, 18]))

x = heaptime(transform_max_heapify([10, 20, 15, 12, 40, 25, 18])).visualize_heap()

#literally just pop biggest element from heap and return the new adjusted heap, by repeating this and continuously popping the max/min element from list
#you can sort stuff this way
def pop_from_heap(an_actual_heap):
    if len(an_actual_heap) <= 1 and len(an_actual_heap) != 0:
        return an_actual_heap.pop() , an_actual_heap
    popelement, an_actual_heap[0] = an_actual_heap[0], an_actual_heap.pop()
    transform_max_heapify(an_actual_heap)
    return popelement, an_actual_heap

#heaptime(pop_from_heap([40, 20, 25, 12, 10, 15, 18])[-1]).visualize_heap()

#heap sort create a min/max heap and keep popping elements from the heap as you go along
def heap_sort(insert_heap):
    list_to_pop = []
    while len(insert_heap) > 0:
        x = pop_from_heap(insert_heap)
        insert_heap = x[-1]
        list_to_pop.insert(0, x[0])
    return list_to_pop
print(heap_sort([40, 20, 25, 12, 10, 15, 18]))

#check if an array is a min heap
def min_heap_check(arr):
    start = len(arr) // 2
    for i in range(start, -1, -1):
        if i*2+1 < len(arr) and arr[i*2+1] < arr[i]:
            return False
        if i*2+2 < len(arr) and arr[i*2+2] < arr[i]:
            return False
    return True
print(min_heap_check([2,10,4,5,3,15]))

"""
#parent = i/2
#left = i * 2
#right= 2i + 1
"""
