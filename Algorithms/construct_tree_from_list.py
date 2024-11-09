class TreeNode:
    def __init__(self, val=0, name="", next=None):
        self.next = next
        self.val = val
        self.name = name

    def __repr__(self):
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))


def build_tree(data: list[int], i, n) -> TreeNode | None:
    if not data:
        return None

    root = None
    if i < n and data[i] is not None:
        root = TreeNode(data[i])
        root.left = build_tree(data, 2 * i + 1, n)
        root.right = build_tree(data, 2 * i + 2, n)
    return root


def main():
    nodes: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    root: TreeNode = build_tree(nodes, 0, len(nodes))
    print(root)


if __name__ == '__main__':
    main()
