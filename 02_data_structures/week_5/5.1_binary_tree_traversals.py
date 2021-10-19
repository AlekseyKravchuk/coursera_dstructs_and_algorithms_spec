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
        self.keys = [0 for i in range(self.n)]
        self.lefts = [0 for i in range(self.n)]
        self.rights = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.keys[i] = a
            self.lefts[i] = b
            self.rights[i] = c

    # <left><root><right> <=> InOrder <=> СИММЕТРИЧНЫЙ порядок обхода
    def inOrder(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return

        # if root is not '-1'(NULL), we first need to visit LEFT subtree
        self.inOrder(self.lefts[i])
        # then we should visit the ROOT node
        self.res_inorder.append(self.keys[i])
        # now we can visit the RIGTH subtree
        self.inOrder(self.rights[i])

    # <root><left><right> <=> PreOrder <=> ПРЯМОЙ порядок обхода
    def preOrder(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1:
            return

        self.res_preorder.append(self.keys[i])
        self.preOrder(self.lefts[i])
        self.preOrder(self.rights[i])

    # <left><right><root> <=> PostOrder <=> ОБРАТНЫЙ порядок обхода, от ДЕТЕЙ идем ОБРАТНО к родителю.
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
        self.inOrder()
        self.res_inorder = " ".join(str(x) for x in self.res_inorder)

        self.preOrder()
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
