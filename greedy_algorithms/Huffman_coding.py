
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

#building huffman tree structure to determine codes
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

#generates a list of all huffman codes for each character in the string to be compressed
def build_codes(root):
    codes = []
    def helper(node, current):
        if not node:
            return
        if not node.left and not node.right:
            codes.append(current+[node.value[0]])
        else:
            helper(node.left, current + ["0"])
            helper(node.right, current + ["1"])
    helper(root, [])
    for x in range(len(codes)):
        codes[x] = ''.join(codes[x])
        codes[x] = (codes[x][-1],codes[x][:-1]) 
    return codes

def encode(string):
    character_occurance = count_character_occurance(string)
    buffmantree = build_tree(character_occurance)
    codelist = build_codes(buffmantree)
    print(codelist)
    codesdict = {} 
    for code in codelist: #loading dictionary for faster code access
        codesdict[code[0]] = code[1]
    build_compressed_string = ""
    for char in string:
        build_compressed_string += codesdict[char]
    return build_compressed_string
    
print(encode("aaaaabccccccddd")) #compressed string for this case is 1111111111100000000101101101

charcount = count_character_occurance("aaaaabccccccddd")
tree = build_tree(charcount)
def decode(encoded_str, tree_head):
    nodetrack = tree_head
    decoded_str = ""
    index = 0
    while len(encoded_str) > index:
        if encoded_str[index] == "0":
            nodetrack = nodetrack.left
        else:
            nodetrack = nodetrack.right
        if nodetrack.value[0] is not None:
            decoded_str += nodetrack.value[0]
            nodetrack = tree_head
        index += 1
    return decoded_str

print(decode("1111111111100000000101101101", tree))