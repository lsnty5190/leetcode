def getNext(s: str):

    next = [-1]
    i = 0
    j = -1

    while i < len(s):

        if j == -1 or s[i] == s[j]:

            i += 1
            j += 1
            next.append(j)

        else:

            j = next[j]

    return next[:len(s)]

def KMP(s, p, next):

    i = -1
    j = -1

    while i < len(s) and j < len(p):

        if j == -1 or s[i] == p[j]:

            i += 1
            j += 1
        
        else:

            j = next[j]

    if j == len(p):

        return i - j

    else:

        return -1

s = 'caabababca'
p = ''
next = getNext(p)
print(next)
index = KMP(s, p, next)
print(index)