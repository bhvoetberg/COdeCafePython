from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def main():
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n9 = TreeNode(9)
    n2 = TreeNode(2, n1, n3)
    n7 = TreeNode(7, n6, n9)
    n4 = TreeNode(4, n2, n7)
    inverted = invert_tree(n4)
    print(inverted)
    print("Hello")

if __name__ == '__main__':
    main()
