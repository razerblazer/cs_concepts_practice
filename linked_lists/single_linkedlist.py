import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head:
        return head
    if head.next:
        x, y = head, head.next
        x.next = swapPairs(y.next)
        y.next = x
        return y
    else:
        return head
    
 
# 2 -> 1 -> 2          3 -> 4
# 1 -> 2 -> 3 -> 4
# 2 -> 1 -> 4 -> 3
def hehexd(head, depth = 0):
    if head.next is None:
        return head, depth % 2 == 1
    next_node, should_flip = hehexd(head.next, depth+1)
    if should_flip:
        head.next = next_node.next
        next_node.next = head
        return next_node, False
    head.next = next_node
    return head, True

def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def create_linked_list(listinput):
    if len(listinput) < 1:
        return
    x = ListNode()
    x.val = listinput[0]
    x.next = create_linked_list(listinput[1:])
    return x

def print_list_result(node):
    lis = []
    while node:
        lis.append(node.val)
        node = node.next
    return lis    
    
    
a = create_linked_list([1,2,3,4,5,6,7])
b = create_linked_list([5,6,43,5])

#print(hehexd(a))
print(print_list_result(a))
a = swapPairs(a)
print(print_list_result(a))
