import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
            return f"{self.val}"


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0

            current_max = max(max_val,node.val)
            print(f"node.val: {node.val}, max val: {max_val}")
            if node.val >= max_val:
                return 1 + dfs(node.left,current_max) + dfs(node.right, current_max)
            return dfs(node.left,current_max) + dfs(node.right, current_max)

        return dfs(root,root.val)


def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """Inserts a value into the BST iteratively."""
    if not root:
        return TreeNode(val)

    current = root
    while True:
        if val < current.val:
            # Go left
            if current.left is None:
                current.left = TreeNode(val)
                return root
            else:
                current = current.left
        else:
            # Go right (or equal)
            if current.right is None:
                current.right = TreeNode(val)
                return root
            else:
                current = current.right

def build_bst_from_list(nums: List[int]) -> Optional[TreeNode]:
    """Builds a BST by inserting elements from a list."""
    if not nums:
        return None

    # First element is the root
    root = TreeNode(nums[0])

    # Insert the rest of the elements
    for val in nums[1:]:
        insert_into_bst(root, val)

    return root

def build_balanced_bst(nums: List[int]) -> Optional[TreeNode]:
    """Builds a height-balanced BST from a sorted list."""

    def sorted_list_to_bst(arr):
        if not arr:
            return None

        # 1. Find the middle element
        mid = len(arr) // 2

        # 2. The middle element becomes the root
        root = TreeNode(arr[mid])

        # 3. Recursively build left subtree from the left half
        root.left = sorted_list_to_bst(arr[:mid])

        # 4. Recursively build right subtree from the right half
        root.right = sorted_list_to_bst(arr[mid + 1:])

        return root

    return sorted_list_to_bst(nums)

def build_binary_tree_from_list(nums: List[Optional[int]]) -> Optional[TreeNode]:
    if not nums or nums[0] is None:
        return None

    root = TreeNode(nums[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nums):
        parent = queue.popleft()
        left_val = nums[i]
        if left_val is not None:
            parent.left = TreeNode(left_val)
            queue.append(parent.left)
        i += 1

        if i < len(nums):
            right_val = nums[i]
            if right_val is not None:
                parent.right = TreeNode(right_val)
                # נוסיף גם אותו לתור
                queue.append(parent.right)
            i += 1

    return root

lst1 = [2,1,1,3,None,1,5]
sol = Solution()
sol.goodNodes(build_binary_tree_from_list(lst1))