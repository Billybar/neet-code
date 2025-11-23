from typing import Optional
from trees.helpers import playground

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

        def dfs(node: TreeNode, mini, maxi )-> bool:
            if node is None:
                return True

            if not (mini <= node.val <= maxi):
                return False

            return dfs(node.left,mini,node.val-1) and dfs(node.right,node.val+1, maxi)

        return dfs(root, NEG_INF, POS_INF)


lst1 = [2,1,3]
sol = Solution()
root1 = playground.build_binary_tree_from_list(lst1)
res = sol.isValidBST(root1)
print(res)