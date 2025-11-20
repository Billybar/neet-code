class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def in_order(root):
    if root:
        in_order(root.left)         # 1. recursive to the left
        print(root.val, end=" ")    # 2. handle the root
        in_order(root.right)        # 3. recursive to the right

def pre_order(root):
    if root:
        print(root.val, end=" ")    # 1. handle the root
        pre_order(root.left)        # 2. recursive to the left
        pre_order(root.right)       # 3. recursive to the right

def post_order(root):
    if root:
        post_order(root.left)       # 1. recursive to the left
        pre_order(root.right)       # 2. recursive to the right
        print(root.val, end=" ")    # 3. handle the root


### BFS ###
import collections

def bfs(root):
    if not root:
        return

    # 1. ניצור תור ריק ונוסיף אליו את השורש
    queue = collections.deque()
    queue.append(root)
    while queue:
        # 3. נוציא את הצומת הראשון בתור
        current_node = queue.popleft()

        # 4. נטפל בו (נדפיס את הערך)
        print(current_node.val, end=" ")

        # 5. נוסיף את הילדים שלו (אם קיימים) לסוף התור
        # (חשוב להוסיף את שמאל לפני ימין כדי לשמור על סדר ההדפסה)
        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

### DFS ##
def dfs_iterative(root):
    """Pre-order."""
    if not root:
        return

    stack = [root]

    while stack:
        # 2.א. הוצאת צומת
        current_node = stack.pop()

        # 2.ב. טיפול בצומת (הדפסה)
        print(current_node.val, end=" ")

        # 2.ג. דחיפת הילד הימני (אם קיים)
        if current_node.right:
            stack.append(current_node.right)

        # 2.ד. דחיפת הילד השמאלי (אם קיים)
        if current_node.left:
            stack.append(current_node.left)



#      1
#    /   \
#   2     3
#  / \
# 4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order (left,root,right):")
in_order(root)
# פלט: 4 2 5 1 3

print("\n\nPre-order (root,left,right):")
pre_order(root)
# פלט: 1 2 4 5 3

print("\n\nPost-order (left,right,root):")
post_order(root)
# פלט: 4 5 2 3 1