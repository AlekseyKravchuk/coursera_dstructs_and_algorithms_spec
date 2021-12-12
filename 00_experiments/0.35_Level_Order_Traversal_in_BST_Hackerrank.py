"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value
sequence. Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def appendNode(self, val):
        if self.root is None:  # there are no any nodes in the given tree
            self.root = Node(val)
        else:  # there are some nodes in the tree already
            current = self.root
            while True:
                if val < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def levelOrderTraversal(self):
        current = self.root
        q = deque()
        q.append(current)

        while q:
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

            print(q.popleft(), end=' ')
            current = q[0] if q else None
        print()

    def getLeaves(self):
        current = self.root
        q = deque()
        leaves = []
        q.append(current)

        while q:
            if current.left is None and current.right is None:
                leaves.append(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

            q.popleft()
            current = q[0] if q else None

        return leaves


if __name__ == '__main__':
    """ Test case input:
    5
    13 20 10 15 12
    """
    n = int(input())
    values = list(map(int, input().split()))
    tree = BinarySearchTree()

    for val in values:
        tree.appendNode(val)

    tree.levelOrderTraversal()
    print(f'leaves of the tree: {tree.getLeaves()}')
