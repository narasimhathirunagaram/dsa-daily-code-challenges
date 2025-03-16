def filter_strings(l,k,m):
    out_l = []
    for i in l:
        vowel_cnt = sum(1 for j in i if j.lower() in 'aeiou')
        if vowel_cnt>=m and len(i)>=k:
            out_l.append(i)
    return out_l

l1,k1,m1 = ["apple","hi","world","yes","python"],4,2
l2,k2,m2 = ["education","science","art","mathematics"],5,3
print(filter_strings(l1,k1,m1))
print(filter_strings(l2,k2,m2))

# Effective:
# def filter_strings(l, k, m):
#     return [s for s in l if len(s) >= k and sum(c in 'aeiouAEIOU' for c in s) >= m]

# l1, k1, m1 = ["apple", "hi", "world", "yes", "python"], 4, 2
# l2, k2, m2 = ["education", "science", "art", "mathematics"], 5, 3

# print(filter_strings(l1, k1, m1))
# print(filter_strings(l2, k2, m2))
