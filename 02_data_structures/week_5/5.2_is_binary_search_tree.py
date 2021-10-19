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
        self.benchmark_lst = sorted(self.keys)

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


def main():
    tree = BinaryTree()
    if tree.n != 0:
        tree.traverse_in_order()
        # tree.print_solution()
        if tree.inorder_traversal_result == tree.benchmark_lst:
            print('CORRECT')
        else:
            print('INCORRECT')
    else:
        print('CORRECT')


threading.Thread(target=main).start()
