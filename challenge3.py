def len_of_last_word(s):
    return len(s.lstrip().split()[-1])

s1 = "Learn Python"
s2 = " coding is fun "
s3 = "  fly  me to  the moon   "

for s in (s1,s2,s3):
    print(len_of_last_word(s))
