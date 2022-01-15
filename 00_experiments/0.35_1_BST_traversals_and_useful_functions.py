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

    # inserts node with given 'val' into given BST
    def insert(self, val):
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

    def search(self, val):
        if self.root is None:
            return
        current = self.root
        while current is not None:
            if val == current.key:
                return current
            elif val < current.key:
                if current.left is not None:
                    current = current.left
                else:
                    return None
            else:  # if val > current.key
                if current.right is not None:
                    current = current.right
                else:
                    return None

    def delete(self, val):
        if self.root is None:
            return False

        # if val in root node
        elif val == self.root.key:
            # TODO
            pass

        parent = None
        node = self.root

        # find node to remove
        while node is not None and node.key != val:
            parent = node
            if val < node.key:
                node = node.left
            elif val > node.key:
                node = node.right

        # case 1: 'val' is not found
        if node is None or node.key != val:
            return False

        # case 2: node to be deleted has no children
        elif node.left is None and node.right is None:
            if parent.left is node:
                parent.left = None
            else:  # if parent.right is node
                parent.right = None
            return True

        # case 3: 'node' to be deleted has only LEFT child
        # but the 'node' itself can be either RIGHT child or LEFT child of parent
        elif node.left is not None and node.right is None:
            if parent.left is node:  # node is LEFT child of it's parent
                parent.left = node.left
            else:  # node is RIGHT child of it's parent
                parent.right = node.left
            return True

        # case 4: 'node' to be deleted has only RIGHT child
        # but the 'node' itself can be either RIGHT child or LEFT child of parent
        elif node.left is None and node.right is not None:
            if parent.left is node:  # node is LEFT child of it's parent
                parent.left = node.right
            else:  # node is RIGHT child of it's parent
                parent.right = node.right
            return True

        # case 5: 'node' to be deleted has both LEFT and RIGHT children
        else:
            parent = node
            current = node.left
            while current is not None:
                parent = current
                current = current.right

    def size_recur(self, node):
        if node is None:
            return 0

        num_of_left_subtree = self.size_recur(node.left)
        num_of_right_subtree = self.size_recur(node.right)
        return 1 + num_of_left_subtree + num_of_right_subtree

    # <left><Root><right>, симметричный обход
    def print_inorder(self, root):
        if root is None:
            return

        self.print_inorder(root.left)
        print(f'{root}({root.level})', end=' ')
        self.print_inorder(root.right)

    def print_level_order(self):
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

    @staticmethod
    def height(node):
        if node is None:
            return -1  # because the height of a leaf should be 0 (-1 + 1 = 0 - that's OK)
        left_subtree_height = BST.height(node.left)
        right_subtree_height = BST.height(node.right)

        return 1 + max(left_subtree_height, right_subtree_height)


if __name__ == '__main__':
    tree = BST()
    # !!!!!!!! Code to take input from standard input !!!!!!!!
    # n = int(input())
    # node_vals_lst = list(map(int, input().split()))
    # for node_val in node_vals_lst:
    #     tree.append_node(node_val)

    node_vals = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
    for val in node_vals:
        tree.insert(val)

    print('In-order traversal:')
    tree.print_inorder(tree.root)
    print()
    print('Level-order traversal:')
    tree.print_level_order()

    # tmp = tree.search(4)
    # print(f'\nResult of searching: {tmp}(level={tmp.level})')

    key2delete = 5
    tree.delete(key2delete)
    print(f'\nLevel-order traversal after deletion {key2delete}:')
    tree.print_level_order()


    # print()
    # print('level-order traversal: ', end='')
    # tree.traverse_level_order()
    # print(f'\nleaves: {tree.get_leaves()}')
    # print(f'REVERSE level-order traversal: {tree.traverse_reverse_level_order()}')
    # print(f'height of BST = {BST.height(tree.root)}')
    # print(f'tree contains {tree.size_recur(tree.root)} nodes')
