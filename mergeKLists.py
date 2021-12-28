from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    out = mergeList(lists)

    return out

def mergeList(lists):

    if not lists:
        return
    if len(lists) == 1:
        return lists[0]

    m = (len(lists)) // 2

    out1, out2 = mergeKLists(lists[:m]), mergeKLists(lists[m:])

    return merge(out1, out2)


def merge(list1: Optional[ListNode], list2: Optional[ListNode]):

    p = list1
    q = list2

    out = ListNode()
    v = out

    # merge
    while q is not None and p is not None:

        if q.val > p.val:

            v.next = p
            v = v.next
            p = p.next

        else:

            v.next = q
            v = v.next
            q = q.next

    while p is not None:

        v.next = p
        v = v.next
        p = p.next

    while q is not None:

        v.next = q
        v = v.next
        q = q.next

    return out.next

lists = [ListNode(val=1, next=ListNode(val= 4, next= ListNode(val= 5, next= None))), ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None))), ListNode(val= 2, next= ListNode(val= 6, next= None))]

out = mergeKLists(lists)

res = []

while out is not None:
    res.append(out.val)
    out = out.next

print(res)