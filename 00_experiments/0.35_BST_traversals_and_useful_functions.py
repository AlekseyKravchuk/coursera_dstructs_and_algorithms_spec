from collections import deque

class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.height = None

    def append_node(self, val):
        if self.root is None:
            self.root = Node(val)
            self.root.level = 0
            self.height = 0
        else:  # self.root is not None => there are already some nodes in the BST
            current = self.root
            while True:
                if val < current.key:
                    if current.left:  # the current node has LEFT child
                        current = current.left
                    else:  # the current node has NOT LEFT child
                        current.left = Node(val)
                        current.left.level = current.level + 1
                        self.height = max(self.height, current.left.level)
                        break
                elif val > current.key:
                    if current.right:  # the current node has RIGHT child
                        current = current.right
                    else:  # the current node has NOT RIGHT child
                        current.right = Node(val)
                        current.right.level = current.level + 1
                        self.height = max(self.height, current.right.level)
                        break
                else:
                    break

    def size_recur(self, node):
        if node is None:
            return 0

        num_of_left_subtree = self.size_recur(node.left)
        num_of_right_subtree = self.size_recur(node.right)
        return 1 + num_of_left_subtree + num_of_right_subtree

    def traverse_level_order(self):
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

    def traverse_reverse_level_order(self):
        if self.root is None:
            return
        q = deque()
        stack = []
        current = self.root
        q.append(current)

        while q:
            if current.right:
                q.append(current.right)
            if current.left:
                q.append(current.left)
            stack.append(q.popleft().key)
            current = q[0] if q else None

        return stack[::-1]

    # returns all leaves in BST using level order traversal algorithm
    def get_leaves(self):
        leaves = []
        if self.root is None:
            return
        q = deque()
        current = self.root
        q.append(current)

        while q:
            if current.left is None and current.right is None:  # there is a LEAF node
                leaves.append(current.key)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            q.popleft()
            current = q[0] if q else None

        return leaves

    def leftRotate(self, grandparent):
        tmp_ptr = grandparent.right
        grandparent.right = tmp_ptr.left
        tmp_ptr.left = grandparent
        return tmp_ptr

    def rightRotate(self, node):
        tmp_ptr = node.left
        node.left = tmp_ptr.right
        tmp_ptr.right = node
        return tmp_ptr

    def rightLeftRotate(self, grandparent):
        # first we need to rotate RIGHT the PARENT node
        grandparent.right = self.rightRotate(grandparent.right)
        # and then we need to rotate LEFT the GRANDPARENT node
        return self.leftRotate(grandparent)

    def leftRightRotate(self, grandparent):
        grandparent.left = self.leftRotate(grandparent.left)
        return self.rightRotate(grandparent)


    @staticmethod
    def height(node):
        if node is None:
            return -1  # because the height of a leaf should be 0 (-1 + 1 = 0 - that's OK)
        left_subtree_height = BST.height(node.left)
        right_subtree_height = BST.height(node.right)

        return 1 + max(left_subtree_height, right_subtree_height)

    # <left><Root><right>, симметричный обход
    @staticmethod
    def traverse_in_order(root):
        if root is None:
            return

        BST.traverse_in_order(root.left)
        print(f'{root}({root.level})', end=' ')
        BST.traverse_in_order(root.right)


if __name__ == '__main__':
    tree = BST()
    n = int(input())
    node_vals_lst = list(map(int, input().split()))
    for node_val in node_vals_lst:
        tree.append_node(node_val)

    BST.traverse_in_order(tree.root)
    BST.rightRotate(tree.root)
    BST.traverse_in_order(tree.root)
    # print()
    # print('level-order traversal: ', end='')
    # tree.traverse_level_order()
    # print(f'\nleaves: {tree.get_leaves()}')
    # print(f'REVERSE level-order traversal: {tree.traverse_reverse_level_order()}')
    # print(f'height of BST = {BST.height(tree.root)}')
    # print(f'tree contains {tree.size_recur(tree.root)} nodes')