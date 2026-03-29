from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # find all the leaf nodes 
    def __init__(self ):
          self.result = 0
    
    # return a list of all distances of leaves to the node
    def dfs(self, node: TreeNode, distance: int ) -> List[int]:
        if not node: 
            return []
        
        if not node.left and not node.right:
            # 表示这个叶子节点的所有叶子节点到它的距离 = 1
            return [1]
        else:
            list_left = []
            list_right = []
            if node.left:
                # 这个等于node的左子树中，所有叶子节点到 node.left的距离，的一个列表
                list_left = self.dfs(node.left, distance)
                # return [x + 1 for x in list_left]

            if node.right:
                # 这个等于node的右子树中，所有叶子节点到 node.right的距离，的一个列表
                list_right = self.dfs(node.right, distance)
                # return [x + 1 for x in list_right]

            if node.left and node.right:
                # 枚举 list_left 与 list_right 之间的所有组合, 有序
                for left in list_left:
                    for right in list_right:
                        if left + right <= distance:
                            self.result += 1
            
            return [x + 1 for x in list_left + list_right]
     
    
    # find all the leaf nodes 
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
          self.dfs(root, distance)

          return self.result


                





        