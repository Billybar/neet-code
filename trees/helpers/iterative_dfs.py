# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        stack = []
        node = root
        last = None
        depths = {}

        while stack or node:
            # if node -> keep going down-left
            if node:
                stack.append(node)
                node = node.left

            # end of branch -> go up
            else:
                node = stack[-1] # peek
                # if no option to down-right
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left,right)
                    last = node
                    node = None

                # go down-right
                else:
                    node = node.right

        return True
