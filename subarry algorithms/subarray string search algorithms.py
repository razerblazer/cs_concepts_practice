#Rabin-karp algorithm
#knuth-Morris-Pratt algorithm
#Aho-Corasick Algorithm

"""
Preprocessing involves processing the given pattern and labels the pattern according to the longest prefix suffix
"""
def preprocessing(pattern):
    if len(pattern) < 1:
        return pattern
    lps = [0]
    leng = 0
    i = 1
    while i < len(pattern):
        if pattern[leng] == pattern[i]:
            leng += 1
            lps.append(leng)
            i += 1
        else:
            if leng > 0:
                leng = lps[leng-1]
            else:
                lps.append(0)
                i += 1
            
    return lps
"""
Actual algorithm takes the preprocessed string and uses the generated to index where to go within the string
"""
def kunth_morris_pratt_pattern_search_algorithm(string, pattern):
    lps = preprocessing(pattern)
    i = j = 0
    indexes = []
    while i < len(string):
        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                indexes.append(i-j)
                j = lps[j-1]
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
            
    return indexes

def hashfunction(pattern, base):
    patternval = 0
    for i in range(len(pattern)):
        patternval += int(ord(pattern[i])) * (base ** (len(pattern)-i-1))
    return patternval

#sliding algorithm but calculates a hash of the given pattern and compares it with each calculated substring hashes
def rabin_karp_algorithm(string, pattern, hashbase):
    patternval = hashfunction(pattern, hashbase)
    rollinghash = hashfunction(string[0:len(pattern)], hashbase)
    indexes = [0 if rollinghash == patternval else None ]
    for x in range(1,len(string)-len(pattern)+1):
        rollinghash -= int(ord(string[x-1])) * (hashbase ** (len(pattern)- 1))
        rollinghash *= hashbase
        rollinghash += int(ord(string[x+len(pattern)-1])) * (hashbase ** 0)
        if patternval == rollinghash:
            indexes.append(x)
    return indexes


def Aho-Corasick_algorithm():
    
    return