#create a max heap structure which depends on the number of occurances of a character in a string


def sort_helper(entry):
    return entry[1]

def count_character_occurance(string):
    count = {}
    for char in string:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1
    hold = []
    for element in count.keys():
        hold.append((element, count[element]))
    hold.sort(key=sort_helper)
    return hold

print(count_character_occurance("absiasnsaijjjdwqkndqwnr"))