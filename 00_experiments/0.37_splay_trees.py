from collections import deque


class Node:
    def __init__(self, key, parent=None, left=None, right=None, ):
        (self.key, self.parent, self.left, self.right) = (key, parent, left, right)

    def __str__(self):
        return str(self.key)


class SplayTree:
    def __init__(self):
        self.root = None

    def appendNode(self, val):
        current = self.root

        if self.root is None:
            self.root = Node(val)
        else:
            while True:
                if val < current.key:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val, current)
                        break
                elif val > current.key:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val, current)
                        break
                else:
                    break

    def print_traverse_level_order(self):
        if self.root is None:
            return
        q = deque()
        current = self.root
        q.append(current)

        while q:
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            print(q.popleft(), end=' ')
            current = q[0] if q else None
        print()

    def splay(self, node):
        if node is None:
            return None

        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            # ZIG (or ZAG) situation
            # if grandparent is None, it means that the node has only one parent being the root node
            if grandparent is None:
                if parent.left is node:
                    rotateRight(self, parent)
                else:
                    rotateLeft(self, parent)

    def rotateRight(self, node):
        tmp_ptr = node.left
        node.left = tmp_ptr.right
        tmp_ptr.right = node
        self.root = tmp_ptr

    def rotateLeft(self, node):
        tmp_ptr = node.right
        node.right = tmp_ptr.left
        tmp_ptr.left = node
        self.root = tmp_ptr


if __name__ == '__main__':
    """
Test input:
5
20 18 15 19 17
    """
    n = int(input())
    node_lst = list(map(int, input().split()))
    splay_tree = SplayTree()

    for node in node_lst:
        splay_tree.appendNode(node)

    splay_tree.print_traverse_level_order()
