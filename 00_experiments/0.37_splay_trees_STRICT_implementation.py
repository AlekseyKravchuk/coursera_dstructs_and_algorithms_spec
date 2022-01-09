"""
https://www.codesdope.com/course/data-structures-splay-trees/
"""

from collections import deque


class Node:
    def __init__(self, val, parent=None):
        self.key = val
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def print_level_order(self):
        if self.root is None:
            return

        current = self.root
        q = deque([current])

        while q:
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)

            print(q.popleft(), end=' ')
            current = q[0] if q else None
        print()

    def left_rotate(self, v):
        if v is None:
            return None
        tmp = v.right
        v.right = tmp.left
        if v.right is not None:
            v.right.parent = v
        tmp.left = v

        tmp.parent = v.parent
        if v.parent is not None:
            if v.parent.left is v:
                v.parent.left = tmp
            else:  # if v.parent.right is v
                v.parent.right = tmp
        else:
            self.root = tmp
        v.parent = tmp

    def right_rotate(self, v):
        if v is None:
            return None
        tmp = v.left
        v.left = tmp.right
        if v.left is not None:
            v.left.parent = v
        tmp.right = v
        tmp.parent = v.parent

        if v.parent is not None:
            if v.parent.left is v:
                v.parent.left = tmp
            else:
                v.parent.right = tmp
        else:
            self.root = tmp
        v.parent = tmp

    def splay(self, v):
        if v is None:
            return None

        while v.parent is not None:  # while 'v' is not root
            if v.parent is self.root:  # 'v' is direct ancestor of root (child of root), so one rotation
                if v.parent.left is v:
                    self.right_rotate(v.parent)
                else:  # if v.parent.right is v
                    self.left_rotate(v.parent)
            else:
                parent = v.parent
                grandparent = parent.parent

                # ZIG-ZIG situation
                if parent.left is v and grandparent.left is parent:  # both are left children
                    self.right_rotate(grandparent)
                    self.right_rotate(parent)

                # ZAG-ZAG situation
                elif parent.right is v and grandparent.right is parent:  # both are right children
                    self.left_rotate(grandparent)
                    self.left_rotate(parent)

                # ZIG-ZAG situation
                elif parent.right is v and grandparent.left is parent:
                    self.left_rotate(parent)
                    self.right_rotate(grandparent)

                # ZAG-ZIG situation
                elif parent.left is v and grandparent.right is parent:
                    self.right_rotate(parent)
                    self.left_rotate(grandparent)
                else:
                    raise ValueError('Logic error happened, there is a bug in splay method.')

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.key:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(val, current)
                        break
                elif val > current.key:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(val, current)
                        break
                else:  # val == current.key => do nothing, break
                    break
        # temporatily disable splay operation on recently accessed node
        # self.splay(n)

    def search(self, val):
        if self.root is None:
            return None
        current = self.root

        while current is not None:
            if val == current.key:
                return current
            elif val < current.key:
                if current.left is not None:
                    current = current.left
                else:
                    return None
            else:  # val > current.key
                if current.right is not None:
                    current = current.right
                else:
                    return None

    def delete(self, val):
        v = self.search(val)
        self.splay(v)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root is not None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root is not None:
            right_subtree.root.parent = None

        if left_subtree.root is not None:
            m = left_subtree.maximum(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

    def print_in_order(self, v):
        if v is None:
            return None

        self.print_in_order(v.left)
        print(v, end=' ')
        self.print_in_order(v.right)


if __name__ == '__main__':
    v = int(input())
    node_lst = list(map(int, input().split()))
    tree = SplayTree()

    for node in node_lst:
        tree.insert(node)

    print(f'inorder traversal BEFORE splaying:', end=' ')
    tree.print_in_order(tree.root)
    print()
    print(f'level-order traversal BEFORE splaying:', end=' ')
    tree.print_level_order()
    print()

    # tmp = tree.search(9)   # for test case #1: /home/kav/splay_trees_input_1.txt
    # tmp = tree.search(24)  # for test case #2: /home/kav/splay_trees_input_2.txt
    tmp = tree.search(17)    # for test case #3: /home/kav/splay_trees_input_3.txt

    tree.splay(tmp)

    print(f'inorder traversal AFTER splaying:', end=' ')
    tree.print_in_order(tree.root)
    print()
    print(f'level-order traversal AFTER splaying:', end=' ')
    tree.print_level_order()
    print()


