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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        node = root

        while stack or node:
            # dive to most left child - smallest
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val
            node = node.right

        return -1
