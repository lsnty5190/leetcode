s = "a"
s = list(s)

def find_max(i, j):

    while(i>=0 and j<len(s) and s[i]==s[j]):
        i, j = i-1, j+1
    
    return s[i+1:j]

out = ''

for t in range(len(s)):

    tmp = find_max(t,t)
    out = tmp if len(tmp) > len(out) else out
    tmp = find_max(t,t+1)
    out = tmp if len(tmp) > len(out) else out 

print(out)
