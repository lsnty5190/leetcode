from collections import deque

s = 'aaa'
s = list(s)

p = 'a*a'
p = list(p)

def isMatch(text, pattern):

    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':

        return isMatch(text, pattern[2:]) or \
                        (first_match and isMatch(text[1:], pattern))
    
    else:
        return first_match and isMatch(text[1:], pattern[1:])

out = isMatch(s, p)
print(out)