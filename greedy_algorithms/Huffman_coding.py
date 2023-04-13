
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
        if tree.value[1] is None:
            constructNode = Node(sortedlist.pop(0))
            if tree.left is None:
                tree.left = constructNode
            else:
                tree.right = constructNode
                tree.value[1] = tree.left.value[1]+tree.right.value[1]
            continue
        else:
            constructNode = Node([None, None])
            if tree.value[1] < sortedlist[0][1]:
                constructNode.left = tree
                constructNode.right = Node(sortedlist.pop(0))
                constructNode.value[1] = constructNode.right.value[1] + constructNode.left.value[1]
            else:
                constructNode.right = tree
                constructNode.left = Node(sortedlist.pop(0))
                constructNode.value[1] = constructNode.right.value[1] + constructNode.left.value[1]
            tree = constructNode
    return tree


def build_codes(root):
    codes = []
    def helper(node, current):
        if not node:
            return
        if not node.left and not node.right:
            codes.append(current)
        else:
            helper(node.left, current + ["0"])
            helper(node.right, current + ["1"])
    helper(root, [])
    for x in range(len(codes)):
        codes[x] = ''.join(codes[x])
    return codes
        
    

x = count_character_occurance("bdddaaaaacccccc")

y = build_tree(x)
print(build_codes(y))
test = ""
while y.left:
    test += "0"
    y = y.left
    
print(test)
