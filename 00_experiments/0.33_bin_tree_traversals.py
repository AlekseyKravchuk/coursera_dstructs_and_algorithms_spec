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

    # in-order <=> СИММЕТРИЧНЫЙ порядок обхода
    # <left><root><right>
    # allows to visit nodes in order (in ascending order)
    def inOrder(self, i=0):
        # BASE case:
        if i == -1:
            return

        self.inOrder(self.lefts[i])
        self.res_inorder.append(self.keys[i])
        self.inOrder(self.rights[i])

    # pre-order <=> ПРЯМОЙ порядок обхода
    # <root><left><right>
    def preOrder(self, i=0):
        # BASE case:
        if i == -1:
            return

        self.res_preorder.append(self.keys[i])
        self.preOrder(self.lefts[i])
        self.preOrder(self.rights[i])

    # post-order <=> ОБРАТНЫЙ порядок обхода, от ДЕТЕЙ идем ОБРАТНО к родителю.
    # <left><right><root>
    def postOrder(self, i=0):
        # BASE case:
        if i == -1:
            return

        self.postOrder(self.lefts[i])
        self.postOrder(self.rights[i])
        self.res_postorder.append(self.keys[i])

    def traverse_all_ways(self):
        self.inOrder()
        self.res_inorder = " ".join(str(x) for x in self.res_inorder)

        self.preOrder()
        self.res_preorder = " ".join(str(x) for x in self.res_preorder)

        self.postOrder()
        self.res_postorder = " ".join(str(x) for x in self.res_postorder)

    def print_solution(self):
        s_inord = 'in-order (СИММЕТРИЧНЫЙ):'
        s_preord = 'pre-order (ПРЯМОЙ):'
        s_postord = 'post-order (ОБРАТНЫЙ):'
        field_width = max(len(s_inord), len(s_preord), len(s_postord)) + 1
        print(f'{s_inord: <{field_width}}{self.res_inorder}')
        print(f'{s_preord: <{field_width}}{self.res_preorder}')
        print(f'{s_postord: <{field_width}}{self.res_postorder}')


def main():
    tree = TreeOrders()
    tree.traverse_all_ways()
    tree.print_solution()


threading.Thread(target=main).start()
