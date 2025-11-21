from tkinter.constants import SOLID
from typing import Optional, List
import playground

NEG_INF = float('-inf')
POS_INF = float('inf')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode, mini:int, maxi:int )-> bool:
            if node is None:
                return True
            if node.left is None and node.right is None:
                return True

            if node.left.val >= node.val or node.right.val <= node.val:
                return False

            if node.left:
                return dfs(node.left,mini,node.val-1)
            if node.right:
                return dfs(node.right,node.val+1, maxi)

            return False

        return dfs(root, int(NEG_INF), int(POS_INF))


lst1 = [2,1,1,3,None,1,5]
sol = Solution
root1 = playground.build_binary_tree_from_list(lst1)
res = sol.isValidBST(root1)
print(res)