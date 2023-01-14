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
# works
def isValidBST(root):
    def valid(node, low, high):
        if not node: return True
        if node.val > low and node.val < high:
            return valid(node.left,low,node.val) and\
                   valid(node.right,node.val,high)
        return False
    return valid(root,-2 ** 31 - 1 ,2 ** 31)

'''Given the root of a binary tree, check whether it is a mirror of itself 
   (i.e., symmetric around its center).'''
def isSymmetricR(root):
    if not root: return True
    def sym(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return sym(left.left,right.right) and\
                   sym(left.right,right.left)
        else:
            return False
    return sym(root.left, root.right)

# non recursive
def isSymmetric(root):
    if not root: return True

    ls = [[root.left, root.right]]

    while len(ls) > 0:
        left, right = ls.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val == right.val:
            ls.insert(0, [left.left,right.right])
            ls.insert(0, [left.right, right.left])
        else:
            return False
    return True

'''Given the root of a binary tree, return the level order traversal of its nodes' values.
 (i.e., from left to right, level by level).'''
def levelOrder(root):
    res, level = [], [root]
    while root and level:
        res.append([node.val for node in level])         
        level = [ch for node in level for ch in (node.left, node.right) if ch]
    return res

if __name__ == '__main__':
    from tree_test import *
    import time
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

    # root = to_binary_tree([2147483647])
    # viz_tree_gpz(root)
    # print(isValidBST(root))
    # root = to_binary_tree([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5])
    # root = to_binary_tree([1,2,2,3,4,4,3])
    # root = to_binary_tree([1,2,2,None,3,None,3])
    # print(isSymmetric(root))
    # start = time.time()
    # isSymmetric(root)
    # end = time.time()
    # print(f'non rec {end - start}')
    # start = time.time()
    # isSymmetricR(root)
    # end = time.time()
    # print(f'rec {end - start}')
    root = to_binary_tree([3,2,9,20,None,None,15,7])
    root = to_binary_tree([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5])
    # root = to_binary_tree([1,2,3,4,None,None,5])
    viz_tree_gpz(root)
    print(levelOrder(root))
    # print(levelOrder(root))
