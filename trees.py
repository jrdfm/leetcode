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
    root = to_binary_tree([])
    viz_tree_gpz(root)
    print(maxDepth(root))