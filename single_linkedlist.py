class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    
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
    while node.val:
        lis.append(node.val)
        node = node.next
        if node.next is None:
            lis.append(node.val)
            node.val = None
    return lis    
    
    
a = create_linked_list([])
b = create_linked_list([])

print(mergeTwoLists(a,b))