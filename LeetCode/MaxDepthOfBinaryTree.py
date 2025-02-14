from typing import Optional


class TreeNode:
    def __init__(self, val=0, name: str = '', left=None, right=None):
        self.val = val
        self.name = name
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    def dfs(root: Optional[TreeNode], depth: int) -> int:
        if not root: return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)


def main():
    node5: TreeNode = TreeNode(5, '5')
    node15: TreeNode = TreeNode(15, '15')
    node7: TreeNode = TreeNode(7, '7', None, node5)
    node9: TreeNode = TreeNode(9, '9')
    node20: TreeNode = TreeNode(20, '20', node15, node7)
    node3: TreeNode = TreeNode(3, '3', node9, node20)
    print(max_depth(node3))


if __name__ == '__main__':
    main()
