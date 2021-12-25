from collections import deque

s = 'aaa'
s = list(s)

p = 'a*a'
p = list(p)

key = deque(p)

query = deque(s)

container = None

while len(query) != 0 and len(key) != 0:

    k = key[0]
    q = query[0]

    # raw check
    if k == q:
        container = k
        key.popleft(), query.popleft()
    # check '.'
    elif k == '.':
        container = k
        key.popleft(), query.popleft()
    # check '*'
    elif k == '*':
        k = container
        if k != '.':
            while(query[0]==k):
                query.popleft()
                if len(query) == 0: break
        else:
            query.clear()
        key.popleft()
    else:
        if key[1] == '*':
            key.popleft()
            key.popleft()
            query.popleft()
        else:
            break

if len(key) != 0 or len(query) != 0:
    print(False)
else:
    print(True)


