from collections import deque


class Node:
    def __init__(self, key, parent=None, left=None, right=None, ):
        (self.key, self.parent, self.left, self.right) = (key, parent, left, right)

    def __str__(self):
        return str(self.key)


class SplayTree:
    def __init__(self):
        self.root = None

    def insertNode(self, val):
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

    def rotateRight(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node

    def rotateLeft(self, node):
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

    def smallRotation(self, v):
        if v.parent is None:
            return
        parent = v.parent
        grandparent = v.parent.parent

        if parent.left is v:
            # Zig situation: node 'v' is LEFT child of its parent
            self.rotateRight(parent)
        else:  # Zag situation: node 'v' is RIGHT child of its parent
            self.rotateLeft(parent)

        # we haven't fixed PARENT attribute for some nodes yet
        # for ZIG situation there are: parent, v and v.right
        # for ZAG situation there are: parent, v and v.left
        self.update(parent)     # fix parent.left.parent and parent.right.parent
        self.update(v)          # fix v.left.parent and v.right.parent
        v.parent = grandparent  # fix v.parent

        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def bigRotation(self, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
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
        if v == None:
            return None
        while v.parent is not None:
            # if grandparent is None, it means that the parent node of 'v' is the root node
            # and given node, 'v', is the LEFT child OR the RIGHT child of a root node
            if v.parent.parent is None:
                self.smallRotation(v)
                break
            self.bigRotation(v)

        self.root = v


if __name__ == '__main__':
    """
Test input:
5
20 18 15 19 17
    """
    n = int(input())
    node_lst = list(map(int, input().split()))
    tree = SplayTree()

    for node in node_lst:
        tree.insertNode(node)

    print('Befor splaying: ', end='')
    tree.print_traverse_level_order()
    tmp_node = tree.search(18)
    # print(tmp_node.left, tmp_node.right)
    tree.splay(tmp_node)
    print('After splaying: ', end='')
    tree.print_traverse_level_order()
