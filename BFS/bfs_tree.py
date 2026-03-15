
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

from collections import deque

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

# 层序遍历,每一层的节点放在一个列表里,最终返回一个包含每层节点列表的列表 [[1], [2, 3], [4, 5, 6], [7]]
def bfs_tree_level_order(root):
     if not root:
        return

     res = []
     q = deque([root])

     while q:
          level = []

          for _ in range(len(q)):
               node = q.popleft()
               level.append(node.val)

               if node.left:
                    q.append(node.left)
               if node.right:
                    q.append(node.right)
               
          res.append(level)
               
             


bfs_tree(root)
