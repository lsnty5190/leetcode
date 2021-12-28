# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def previsitl(root: TreeNode, res):

#     if root is not None:

#         res.append(root.val)
#         previsitl(root.left, res)
#         previsitl(root.right, res)

# def previsitr(root: TreeNode, res):

#     if root is not None:

#         res.append(root.val)
#         previsitr(root.right, res)
#         previsitr(root.left, res)

# def isSymmetric(root: TreeNode):

#     l = root.left
#     r = root.right

#     lout = []
#     rout = []
#     previsitl(l, lout)
#     previsitr(r, rout)

#     print(lout)
#     print(rout)

#     return lout == rout

# root = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 3, left= None, right= None), right= TreeNode(val= 4, left= None, right= None)), right= TreeNode(val= 2, left= TreeNode(val= 4, left= None, right= None), right= TreeNode(val= 3, left= None, right= None)))
# res = isSymmetric(root)
# print(res)

from torch_geometric.nn import GATConv

a = [1,2,3]
print(a.pop(0))