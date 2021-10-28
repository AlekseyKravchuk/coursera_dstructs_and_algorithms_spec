# python3

import sys
import threading
from collections import namedtuple

Node = namedtuple('Node', ['key', 'node_index'])

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class BinaryTree:
    def __init__(self):
        self.res = []
        self.state = ''
        self.BST_flag = True

        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.lefts = [0 for _ in range(self.n)]
        self.rights = [0 for _ in range(self.n)]

        for i in range(self.n):
            self.keys[i], self.lefts[i], self.rights[i] = map(int, sys.stdin.readline().split())

        self.sorted_BST_keys = sorted(self.keys)
        self.root_key = self.keys[0]

    # TODO
    # <left><root><right> <=> In-Order <=> СИММЕТРИЧНЫЙ порядок обхода
    def in_order(self, i=0):
        # BASE case: if a tree or subtree is empty, return
        if i == -1 or self.BST_flag is False:
            return

        # traverse left subtree
        self.in_order(self.lefts[i])

        # check if given TREE is consistent with BST rule
        if self.res:
            # do a check
            if self.res[-1].key == self.keys[i]:
                if self.lefts[self.res[-1].node_index] == i:
                    self.BST_flag = False
                    return
        elif self.root_key == self.keys[i]:
            self.BST_flag = False
            return
        # if a test succeeds, then visit ROOT node (add its key to resulting array)
        self.res.append(Node(self.keys[i], i))

        # traverse right subtree
        self.in_order(self.rights[i])

    def is_almost_BST(self):
        lst2compare = [node.key for node in self.res]
        if lst2compare == self.sorted_BST_keys:
            return True
        else:
            return False

    def solve_is_a_BST_advanced(self):
        if self.n == 0:
            self.state = 'CORRECT'
        else:
            self.in_order()
            if self.BST_flag is True and self.is_almost_BST():
                self.state = 'CORRECT'
            else:
                self.state = 'INCORRECT'

        print(self.state)


def main():
    tree = BinaryTree()
    tree.solve_is_a_BST_advanced()


threading.Thread(target=main).start()
