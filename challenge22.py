# Leetcode 408 https://leetcode.com/problems/valid-word-abbreviation/description/ 

def splitString(s):
    l = []
    temp = ''
    for i in s:
        if i.isnumeric():
            temp += i
        else:
            if temp:
                l.append(int(temp))
                temp = ''
            l.append(i)
    return l 

def isValid(word,l):
    ind = 0
    for i in range(len(l)):
        print(l[i],word[ind])
        if isinstance(l[i],str):
            if l[i] == word[ind]:
                ind += 1
            else:
                return False
        else:
            ind += l[i]
    return True


# s = 'i12iz4n'
# word = 'internationalization'
abbr = 'a2e'
word = 'apple'
l = splitString(abbr)
ind = 0
print(isValid(word,l))
