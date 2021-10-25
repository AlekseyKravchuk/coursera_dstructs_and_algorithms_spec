# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class BinaryTree:
    def __init__(self):
        self.inorder_traversal_result = []
        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.lefts = [0 for _ in range(self.n)]
        self.rights = [0 for _ in range(self.n)]

        for i in range(self.n):
            self.keys[i], self.lefts[i], self.rights[i] = map(int, sys.stdin.readline().split())

        self.state = 'INCORRECT'
        self.sorted_BST_keys = sorted(self.keys)

    # <left><root><right> <=> InOrder <=> СИММЕТРИЧНЫЙ порядок обхода
    def traverse_in_order(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return

        # if root is not '-1'(NULL), we first need to visit LEFT subtree
        self.traverse_in_order(self.lefts[i])
        # then we should visit the ROOT node
        self.inorder_traversal_result.append(self.keys[i])
        # now we can visit the RIGTH subtree
        self.traverse_in_order(self.rights[i])

    # TODO !!!!!!!
    # check definition of BST using pre-order traversal (ПРЯМОЙ порядок обхода)
    # <ROOT><left><right>
    def check_definition_BST(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return
        if self.res_preorder and self.res_preorder[-1] == self.keys[i]:
            return False
        else:
            self.res_preorder.append(self.keys[i])
            self.pre_order(self.lefts[i])
            self.pre_order(self.rights[i])

    def solve_is_a_BST_advanced(self):
        if self.n == 0:
            self.state = 'CORRECT'
        else:
            self.traverse_in_order()
            if self.inorder_traversal_result == self.sorted_BST_keys:
                self.state = 'CORRECT'

        print(self.state)


def main():
    tree = BinaryTree()
    tree.solve_is_a_BST_advanced()


threading.Thread(target=main).start()
