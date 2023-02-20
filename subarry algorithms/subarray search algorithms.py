#boyer-moore algorithm
#Rabin-karp algorithm
#knuth-Morris-Pratt algorithm

"""
Preprocessing involves processing the given pattern and labels the pattern
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
def kunth_morris_pratt_pattern_search_algorithm(string, pattern):
    return

#
def boyer_moore_algorithm():
    return


print(preprocessing("ABABD"))