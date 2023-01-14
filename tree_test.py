#!/usr/local/bin/python 
# Imports for graphviz
from graphviz import Digraph
import random


class TreeNode: 
  def __init__(self, val): 
    self.val = val 
    self.left = None
    self.right = None
    self.id = random.random()


def to_binary_tree(list):
    if not list:
        return None

    it = iter(list)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


def to_binary_tree(list): 
  if not list: 
    return None 

  root = TreeNode(list[0]) 
  q = [root] 
  i = 1
  while i < len(list): 
    node = q.pop(0) 

    if list[i] is not None: 
      node.left = TreeNode(list[i]) 
      q.append(node.left) 
    
    i += 1
    if i < len(list) and list[i] is not None: 
      node.right = TreeNode(list[i]) 
      q.append(node.right) 

    i += 1

  return root 

# Function to print level order traversal of tree 
def level_order_traversal(root): 
  if root is None: 
    return 
  q = [] 
  d = {}
  q.append(root) 
 
  while (len(q)) > 0: 
    print(q[0].val, end=" ") 
    node = q.pop(0) 
    if node.left is not None: 
      q.append(node.left) 
    
    if node.right is not None: 
      q.append(node.right) 







def viz_tree_gpz(root): 
  dot = Digraph(format = 'png')

  q = [] 
  q.append(root) 
  if not root:
      return None
  while (len(q)) > 0: 
    node = q.pop(0) 

    # make_node_in_gvz(node, dot)
    dot.node(str(node.id),label = str(node.val),shape='circle',fixedsize='true')

    if node.left is not None: 
      q.append(node.left) 
      dot.edge(str(node.id), str(node.left.id))
    
    if node.right is not None: 
      q.append(node.right)
      dot.edge(str(node.id), str(node.right.id)) 

#   print(dot.source)
  dot.render('test', view=True) 



# Driver Code 
if __name__ == '__main__': 
  random.seed(42)
  arr = [1, 2, 3, 4, 5, -1, 6, -1, -1, 7, 8] 
  root = to_binary_tree(arr) 
  level_order_traversal(root) 
#   viz_tree_gpz(root)

  root = to_binary_tree([3,9,20,None,None,15,7])
  viz_tree_gpz(root)