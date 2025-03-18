def longest_substring(s):
    left = 0
    mx = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            # print("Left assigned to: ", left, s[left])
        char_set.add(s[right])
        # print("Index: ",right, "Char set:", char_set)
        mx = max(mx,right-left+1)
        # print("Mx: ", mx)
    return mx
    

input1 = "abcabcbb"
input2 = "bbbbb"
input3 = "pwwkew"

print(longest_substring(input1))
print(longest_substring(input2))
print(longest_substring(input3))