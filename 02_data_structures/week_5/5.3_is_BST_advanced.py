# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class BinaryTree:
    def __init__(self):
        self.res = []
        self.state = ''

        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.lefts = [0 for _ in range(self.n)]
        self.rights = [0 for _ in range(self.n)]

        for i in range(self.n):
            self.keys[i], self.lefts[i], self.rights[i] = map(int, sys.stdin.readline().split())

        self.sorted_BST_keys = sorted(self.keys)

    # TODO
    # <left><root><right> <=> InOrder <=> СИММЕТРИЧНЫЙ порядок обхода
    def in_order_advanced(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1 or self.is_satisfied is False:
            return

        # if root is not '-1'(NULL), we first need to visit LEFT subtree
        self.in_order_advanced(self.lefts[i])
        # then we should visit the ROOT node

        # if len(self.res) > 1:
        #     if self.res[-2] >= self.res[-1]:
        #         self.is_satisfied = False
        #         return

        if self.res:
            if self.res[-1] >= self.keys[i]:
                self.is_satisfied = False
                return

        self.res.append(self.keys[i])
        # now we can visit the RIGHT subtree
        self.in_order_advanced(self.rights[i])

    def solve_is_a_BST_advanced(self):
        if self.n == 0:
            self.state = 'CORRECT'
        else:
            self.in_order_advanced()
            if self.is_satisfied and self.res == self.sorted_BST_keys:
                self.state = 'CORRECT'
            else:
                self.state = 'INCORRECT'

        print(self.state)


def main():
    tree = BinaryTree()
    tree.solve_is_a_BST_advanced()


threading.Thread(target=main).start()
