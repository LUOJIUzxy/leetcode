from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)

def bfs_tree(root):
     if not root:
         return # 处理空树的情况
     
     queue = deque([root])

     while queue:
          node = queue.popleft()
          print(node.val)

          if node.left:
             queue.append(node.left)
          if node.right:
              queue.append(node.right)
             


bfs_tree(root)
