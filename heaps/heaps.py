#max/min heapify, pop, add new value+balance, heap search
import math
from io import StringIO
import heapq

class heaptime:
    def __init__(self, arr=[]):
        self.heap = arr

    def add(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        parent = (current - 1) // 2
        # Compare and swap with parent until the value is larger or it's at the root
        while current > 0 and self.heap[current] > self.heap[parent]:
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = (current - 1) // 2

    def remove(self):
        if not self.heap:
            return None
        maximum = self.heap[0]
        last_leaf = self.heap.pop()
        if self.heap:
            self.heap[0] = last_leaf
            current = 0
            left_child = current * 2 + 1
            right_child = current * 2 + 2
            # Compare and swap with larger child until the value is smaller or it's at a leaf node
            while (left_child < len(self.heap) and last_leaf < self.heap[left_child]) or (right_child < len(self.heap) and last_leaf < self.heap[right_child]):
                if left_child < len(self.heap) and (right_child >= len(self.heap) or self.heap[left_child] > self.heap[right_child]):
                    self.heap[current], self.heap[left_child] = self.heap[left_child], self.heap[current]
                    current = left_child
                else:
                    self.heap[current], self.heap[right_child] = self.heap[right_child], self.heap[current]
                    current = right_child
                left_child = current * 2 + 1
                right_child = current * 2 + 2
        return maximum

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
"""
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    return arr
"""

def insert_helper(arr, position):
    if position == 0:
        return
    parent = (position // 2) - 1
    if arr[position] > arr[parent]:
        arr[parent], arr[position] = arr[position], arr[parent]
    insert_helper(arr, parent)
    
    
#insert into max heap by insertion(insert elements one by one and modify heap as required) O(nlogn)
def max_insertion(insert, arr):
    arr.append(insert)
    insert_helper(arr, len(arr)-1)
    return arr

test = [-97, -37, -91, -12, -5, -90, -64, -1, -6]
heapq.heapify(test)
print(max_insertion(6, [97, 37, 91, 12, 5, 90, 64, 1]))
print(test)
o = heaptime(test)
p = heaptime(max_insertion(6, [97, 37, 91, 12, 5, 90, 64, 1]))
o.visualize_heap()
p.visualize_heap()
#heapify(start from end and modify going up)


x = [5, 12, 64, 1, 37, 90, 91, 97]
"""
for i in range(len(x)):
    p.append(-x[i])

y = heaptime(build_max_heap(x))
y.visualize_heap()
print(x)


b=heapq.heapify(p)
print(p)
a = heaptime(p)
a.visualize_heap()
"""

"""
print(heaptime.heap)
heaptime.visualize_heap()
#parent = i/2
#left = i * 2
#right= 2i + 1
heaptime.max_heapify()
print(heaptime.heap)
heaptime.visualize_heap()
"""
