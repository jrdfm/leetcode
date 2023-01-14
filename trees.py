#!/usr/local/bin/python 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''Given the root of a binary tree, return its maximum depth.'''
def maxDepth(root):
    if not root:
        return 0
    if root.left:
        left = 1 + maxDepth(root.left)
    else:
        left = 1
    if root.right:
        right = 1 + maxDepth(root.right)    
    else:
        right = 1
    return max(left, right)

'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).'''
def isValidBST(root):
    if not root:
        return False
    if root.left:
        left = (root.val > root.left.val) and isValidBST(root.left)
    else:
        left = True
    if root.right:
        right = (root.val < root.right.val) and isValidBST(root.right) 
    else:
        right = True
    return left and right  

def isValidBST(root):
    def valid(node, low, high):
        if not node: return True
        if node.val > low and node.val < high:
            return valid(node.left,low,node.val) and\
                   valid(node.right,node.val,high)
        return False
    return valid(root,-2 ** 31 - 1 ,2 ** 31)
            
# def isValidBST(root):
    
#     def validate(node, lower, upper):
#         if not node:  return True    # empty node/Tree considered BST

#         # compare the node range is still valid: between low and high
#         if node.val > lower and node.val < upper:
#             return validate(node.left, lower, node.val) and \
#                     validate(node.right, node.val, upper)
#         return False
#     return validate(root, float("-inf"), float("+inf")) # <--- miss here!
if __name__ == '__main__':
    from tree_test import *
    random.seed(42)

    # root = to_binary_tree([3,9,20,None,None,15,7])
    # viz_tree_gpz(root)
    # print(maxDepth(root))

    # root = to_binary_tree([1,None,2])
    # viz_tree_gpz(root)
    # print(maxDepth(root))
    # root = to_binary_tree([1, 2, 3, 4, 5, -1, 6, -1, -1, 7, 8] )
    # viz_tree_gpz(root)
    # print(maxDepth(root))
    # root = to_binary_tree([3,9,20,None,None,15,7])
    # viz_tree_gpz(root)
    # print(maxDepth(root))
    # root = to_binary_tree([])
    # viz_tree_gpz(root)
    # print(maxDepth(root))

    # root = to_binary_tree([2,1,3])
    # viz_tree_gpz(root)
    # print(isValidBST(root))

    # root = to_binary_tree([5,1,4,None,None,3,6])
    # viz_tree_gpz(root)
    # print(isValidBST(root))

    # root = to_binary_tree([5,4,6,None,None,3,7])
    # viz_tree_gpz(root)
    # print(isValidBST(root))

    root = to_binary_tree([2147483647])
    viz_tree_gpz(root)
    print(isValidBST(root))
