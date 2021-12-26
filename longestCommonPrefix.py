class Node:

    def __init__(self, val=None, lchild=None, rchild=None) -> None:
        
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

def consruct_tree(nums):

    root = Node(nums[0])

    p, q = root, None

    for i in range(1, len(nums)):

        while p is not None:
            
            q = p

            if nums[i] >= p.val:
                p = p.rchild
            elif nums[i] < p.val:
                p = p.lchild

        tmp = Node(val=nums[i])
        
        