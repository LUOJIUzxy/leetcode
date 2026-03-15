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


def dfs_tree_preorder(node):
     if not node:
          return

     print(node.val)

     dfs_tree_preorder(node.left)
     dfs_tree_preorder(node.right)

def dfs_tree_inorder(node):
     if not node:
          return
     dfs_tree_inorder(node.left)
     print(node.val)
     dfs_tree_inorder(node.right)

def dfs_tree_postorder(node):
     if not node:
          return
     dfs_tree_postorder(node.left)

     dfs_tree_postorder(node.right)
     print(node.val)


dfs_tree_postorder(root)