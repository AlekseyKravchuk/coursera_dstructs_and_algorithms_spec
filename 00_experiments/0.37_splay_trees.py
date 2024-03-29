from collections import deque


class Node:
    def __init__(self, key, parent=None, left=None, right=None, ):
        (self.key, self.parent, self.left, self.right) = (key, parent, left, right)

    def __str__(self):
        return str(self.key)


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
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
    
    def search(self, val):
        current = self.root
        if self.root is None:
            return None
        else:
            while True:
                if val == current.key:
                    return current
                elif val < current.key:
                    if current.left:
                        current = current.left
                    else:
                        return None
                else:  # val > current.key
                    if current.right:
                        current = current.right
                    else:
                        return None

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

    def right_rotate(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node

    def left_rotate(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node

    # updates 'PARENT' attribute for LEFT and RIGHT child of node 'v'
    @staticmethod
    def update(v):
        if v is None:
            return
        if v.left is not None:
            v.left.parent = v
        if v.right is not None:
            v.right.parent = v

    def smallRotation(self, node):
        if node.parent is None:
            return None
        parent = node.parent
        grandparent = node.parent.parent

        if parent.left is node:
            # Zig situation: node 'v' is LEFT child of its parent
            self.right_rotate(parent)
        else:  # Zag situation: node 'v' is RIGHT child of its parent
            self.left_rotate(parent)

        # we haven't fixed PARENT attribute for some nodes yet
        # for ZIG situation there are: parent, v and v.right
        # for ZAG situation there are: parent, v and v.left
        self.update(parent)     # fix parent.left.parent and parent.right.parent
        self.update(node)          # fix v.left.parent and v.right.parent
        node.parent = grandparent  # fix v.parent

        # there is one issue left: we should attach modified subtree to unmodified one
        if grandparent is not None:
            if grandparent.left is parent:
                grandparent.left = node
            else:
                grandparent.right = node

    def bigRotation(self, v):
        if v.parent.left is v and v.parent.parent.left is v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        elif v.parent.right is v and v.parent.parent.right is v.parent:
            # Zag-zag
            self.smallRotation(v.parent)
            self.smallRotation(v)
        else:
            # Zig-zag
            self.smallRotation(v)
            self.smallRotation(v)

    def splay(self, v):
        if v is None:
            return None
        while v.parent is not None:
            # if the node 'v' is the direct child of root (LEFT or RIGHT child of root), we will just do 1 rotation
            if v.parent.parent is None:
                self.smallRotation(v)
                break
            # otherwise
            self.bigRotation(v)

        self.root = v


if __name__ == '__main__':
    """
Test input #1:
5
20 18 15 19 17

Test input #2:
5
15 12 18 14 13

Test input #3:
4
15 12 10 9
    """
    n = int(input())
    node_lst = list(map(int, input().split()))
    tree = SplayTree()

    for node in node_lst:
        tree.insert(node)

    print('Before splaying: ', end='')
    tree.print_traverse_level_order()
    # tmp_node = tree.search(18)
    tmp_node = tree.search(9)
    # print(tmp_node.left, tmp_node.right)
    tree.splay(tmp_node)
    print('After splaying: ', end='')
    tree.print_traverse_level_order()
