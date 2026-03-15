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


def dfs_tree(node):
     if not node:
          return

     print(node.val)

     dfs_tree(node.left)
     dfs_tree(node.right)


dfs_tree(root)