
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sort_helper(entry):
    return entry[1]
#using sort instead of building minheap(code generated is slightly different)
def count_character_occurance(string):
    count = {}
    for char in string:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1
    hold = []
    for element in count.keys():
        hold.append([element, count[element]])
    hold.sort(key=sort_helper)
    return hold



def build_tree(sortedlist):
    tree = Node([None,None])
    while sortedlist != []:
        if tree.left is None:
            tree.left = sortedlist.pop(0)
            continue
        elif tree.right is None:
            tree.right = sortedlist.pop(0)
            tree.value[1] = tree.left[1]+tree.right[1]
            continue
        constructNode = Node([None, None])
        if tree.value[1] < sortedlist[0][1]:
            constructNode.left = tree
            constructNode.right = sortedlist.pop(0)
            constructNode.value[1] = constructNode.right[1] + constructNode.left.value[1]
        else:
            constructNode.right = tree
            constructNode.left = sortedlist.pop(0)
            constructNode.value[1] = constructNode.right.value[1] + constructNode.left[1]
        tree = constructNode
        
    return tree
            
x = count_character_occurance("absiasnsaijjjdwqkndqwnr")
print(x)
y = build_tree(x)
print(y)
test = ""
while True:
    if not isinstance(y.right, Node):
        test += "0"
        break
    test += "0"
    y = y.right
    
print(test)
