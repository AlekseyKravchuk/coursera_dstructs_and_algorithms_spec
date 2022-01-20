# Binary Search Tree in Python
# code basis: https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py
# explanation: https://www.youtube.com/watch?v=LSju119w8BE
from collections import deque


class Node:
    # class variable
    inorder_lst = []

    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def insert(self, val):
        if self.key == val:
            return False

        elif self.key > val:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
                return True

        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
                return True

    def search_recursive(self, val):
        if self.key == val:
            return True
        elif val < self.key:
            if self.left is not None:
                return self.left.search_recursive(val)
            else:
                return False
        else:  # if val > self.key
            if self.right is not None:
                return self.right.search_recursive(val)
            else:
                return False

    def getInorderSuccessor(self):
        current = self.right
        while current is not None and current.left is not None:
            current = current.left
        return current

    @staticmethod
    def delNode(root, val2del):
        if root is None:
            return None

        if val2del < root.key:
            root.left = root.delNode(root.left, val2del)
        elif val2del > root.key:
            root.right = root.delNode(root.right, val2del)
        else:
            # val2del == root.key, so we found node to be deleted. There are following possible cases:
            # 1) leaf node 2) has only LEFT child 3) has only RIGHT child 4) has both the LEFT and RIGHT children
            if root.left is None:  # so root.right can be either None or not None, so cases 1) and 3)
                return root.right
            elif root.right is None:  # root.left is not None and root.right is None, so case 2)
                return root.left
            else:  # case 4)
                isuc = root.getInorderSuccessor()
                root.key = isuc.key
                root.right = root.delNode(root.right, isuc.key)

        return root

    def get_height(self):
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1

    def print_preorder(self):
        if self is not None:
            print(self)
            if self.left:
                self.left.print_preorder()
            if self.right:
                self.right.print_preorder()

    def print_postorder(self):
        if self is not None:
            if self.left:
                self.left.print_postorder()
            if self.right:
                self.right.print_postorder()
            print(self.key)

    def print_inorder(self):
        if self is not None:
            if self.left:
                self.left.print_inorder()
            print(self, end=' ')
            if self.right:
                self.right.print_inorder()

    def generate_inorder_lst(self):
        # TODO
        if self is not None:
            if self.left:
                self.left.generate_inorder_lst()
            Node.inorder_lst.append(str(self.key))
            if self.right:
                self.right.generate_inorder_lst()


class BST:
    def __init__(self):
        self.root = None
        self.inorder_lst = []

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def find(self, data):
        if self.root:
            return self.root.search_recursive(data)
        else:
            return False

    def get_height(self):
        if self.root:
            return self.root.get_height()
        else:
            return -1

    def delete_iterative(self, val):
        # empty tree
        if self.root is None:
            return False

        # self.root is not None and 'val' is in root node
        elif self.root.key == val:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left is not None and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right is not None:
                self.root = self.root.right
            elif self.root.left is not None and self.root.right is not None:
                # search for inorder successor ('isuc') of 'self.root' node in right subtree
                isuc_parent = self.root
                isuc = self.root.right
                while isuc.left is not None:
                    isuc_parent = isuc
                    isuc = isuc.left

                self.root.key = isuc.key

                if isuc.right is not None:
                    if isuc is isuc_parent.left:
                        isuc_parent.left = isuc.right
                    elif isuc is isuc_parent.right:
                        isuc_parent.right = isuc.right
                else:
                    if isuc is isuc_parent.left:
                        isuc_parent.left = None
                    elif isuc is isuc_parent.right:
                        isuc_parent.right = None
            return True

        # tree is not empty and 'val' is not in root node => so search for the node 'v' to be deleted
        v_parent = None
        v = self.root

        # right after while loop node 'v' will point to the node to be deleted and 'v_parent' will point to its parent
        while v is not None and v.key != val:
            v_parent = v
            if val < v.key:
                v = v.left
            elif val > v.key:
                v = v.right

        # case 1: 'val' is not found in the tree
        if v is None or v.key != val:
            return False

        # case 2: delete 'v' having no children
        elif v.left is None and v.right is None:
            if v is v_parent.left:
                v_parent.left = None
            elif v is v_parent.right:
                v_parent.right = None
            return True

        # case 3: delete 'v' having only LEFT child
        elif v.left is not None and v.right is None:
            if v is v_parent.left:
                v_parent.left = v.left
            elif v is v_parent.right:
                v_parent.right = v.left
            return True

        # case 4: delete 'v' having only RIGHT child
        elif v.left is None and v.right is not None:
            if v is v_parent.left:
                v_parent.left = v.right
            elif v is v_parent.right:
                v_parent.right = v.right
            return True

        # case 5: delete 'v' having both LEFT & RIGHT children
        else:  # v.left is not None and v.right is not None
            # search inorder successor ('isuc') of node 'v' in the right subtree
            # i.e. search for node having MINIMUM key in RIGHT subtree of node 'v' ('v' is the node to delete)
            isuc_parent = v
            isuc = v.right
            while isuc.left is not None:
                isuc_parent = isuc
                isuc = isuc.left

            v.key = isuc.key

            # when inorder successor has right subtree
            if isuc.right is not None:
                # if 'isuc' is LEFT child of its v_parent ('isuc_parent')
                if isuc is isuc_parent.left:
                    isuc_parent.left = isuc.right

                # if 'isuc' is RIGHT child of its v_parent ('isuc_parent')
                elif isuc is isuc_parent.right:
                    isuc_parent.right = isuc.right

            # when inorder successor has NO right subtree, so it is a LEAF node
            else:  # if isuc.right is None
                if isuc is isuc_parent.left:
                    isuc_parent.left = None
                elif isuc is isuc_parent.right:
                    isuc_parent.right = None
            return True

    # wraper method in order to allow method to be called without passing root.node explicitly
    def delete_recursive(self, val):
        if self.root is not None:
            self.root = self.root.delNode(self.root, val)

    def print_preorder(self):
        if self.root is not None:
            print("PreOrder:", end=' ')
            self.root.print_preorder()

    def print_postorder(self):
        if self.root is not None:
            print("PostOrder:", end=' ')
            self.root.print_postorder()

    def print_inorder(self):
        if self.root is not None:
            print("InOrder:", end=' ')
            self.root.print_inorder()
            print()

    def get_inorder_lst(self):
        if self.root is not None:
            if Node.inorder_lst:
                Node.inorder_lst = []
            self.root.generate_inorder_lst()
            return Node.inorder_lst

    def print_level_order(self):
        if self.root is None:
            return

        level_ordered_lst = []
        q = deque()
        current = self.root
        q.append(current)

        while q:
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            level_ordered_lst.append(q.popleft())
            current = q[0] if q else None
        print('Level-order:', end=' ')
        print(*level_ordered_lst)


if __name__ == '__main__':
    tree = BST()
    # !!!!!!!! Code to take input from standard input !!!!!!!!
    n = int(input())
    values = list(map(int, input().split()))
    val2delete = int(input())

    for val in values:
        tree.insert(val)

    tree.print_inorder()
    tree.print_level_order()
    print(f'val2delete = {val2delete}')

    # print('Inorder list: {0}'.format(' '.join(tree.get_inorder_lst())))
    # inorder_lst_before = tree.get_inorder_lst()
    # tree.delete_iterative(val2delete)
    tree.delete_recursive(val2delete)

    # inorder_lst_after = tree.get_inorder_lst()
    # if inorder_lst_before != inorder_lst_after:
    #     print("Something is broken, BST invariant doesn't stay unchanged after last operation.")
    print()
    print(f'After deletion of node {val2delete}: ')
    tree.print_level_order()
    tree.print_inorder()
