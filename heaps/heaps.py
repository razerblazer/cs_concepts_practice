#max/min heapify, pop, print visualizer, add new value+balance, heap search
class heaptime:
    def __init__(self,heap=None):
        self.heap = []

    def create_rough_heap(self,lis):
        for x in lis:
            self.heap.append(x)
        return self.heap

#heaptime = heaptime()
#heaptime.create_rough_heap([1,2,3,4,5,56,2])
#print(heaptime.heap)