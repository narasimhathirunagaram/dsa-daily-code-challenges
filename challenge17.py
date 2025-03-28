# Leetcode: 522
def is_subsequence(s1, s2):
    i = 0
    for ch in s2:
        if i < len(s1) and s1[i] == ch:
            i += 1
    return i == len(s1)

def find_LUS_length(strs):
    strs.sort(key=len, reverse=True)

    for i, s in enumerate(strs):
        found = False
        for j, other in enumerate(strs):
            if i != j and is_subsequence(s, other):
                found = True
                break
        if not found:
            return len(s)
    
    return -1


if __name__ == '__main__':
    print(find_LUS_length(["aba", "cdc", "eae"]))  # Output: 3
    print(find_LUS_length(["aaa", "aaa", "aa"]))   # Output: -1