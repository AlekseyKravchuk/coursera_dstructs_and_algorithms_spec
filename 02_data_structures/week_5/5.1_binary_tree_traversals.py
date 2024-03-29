# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.res_preorder = []
        self.res_inorder = []
        self.res_postorder = []

        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.lefts = [0 for _ in range(self.n)]
        self.rights = [0 for _ in range(self.n)]
        for i in range(self.n):
            self.keys[i], self.lefts[i], self.rights[i] = map(int, sys.stdin.readline().split())

    # in-order <=> СИММЕТРИЧНЫЙ порядок обхода
    # <left><root><right>
    # allows to visit nodes in order (in ascending order)
    def in_order(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return

        # if root is not '-1'(NULL), we first need to visit LEFT subtree
        self.in_order(self.lefts[i])
        # then we should visit the ROOT node
        self.res_inorder.append(self.keys[i])
        # now we can visit the RIGTH subtree
        self.in_order(self.rights[i])

    # pre-order <=> ПРЯМОЙ порядок обхода
    # <root><left><right>
    def pre_order(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return

        self.res_preorder.append(self.keys[i])
        self.pre_order(self.lefts[i])
        self.pre_order(self.rights[i])

    # post-order <=> ОБРАТНЫЙ порядок обхода, от ДЕТЕЙ идем ОБРАТНО к родителю.
    # <left><right><root>
    def postOrder(self, i=0):
        # BASE case:
        if i == -1:
            return

        # if root is not '-1'(NULL), we first need to visit LEFT subtree
        self.postOrder(self.lefts[i])
        # then we should visit RIGHT subtree
        self.postOrder(self.rights[i])
        # now we can visit the ROOT node
        self.res_postorder.append(self.keys[i])

    def traverse_all_ways(self):
        self.in_order()
        self.res_inorder = " ".join(str(x) for x in self.res_inorder)

        self.pre_order()
        self.res_preorder = " ".join(str(x) for x in self.res_preorder)

        self.postOrder()
        self.res_postorder = " ".join(str(x) for x in self.res_postorder)

    def print_solution(self):
        print(self.res_inorder)
        print(self.res_preorder)
        print(self.res_postorder)


def main():
    tree = TreeOrders()
    tree.traverse_all_ways()
    tree.print_solution()


threading.Thread(target=main).start()
