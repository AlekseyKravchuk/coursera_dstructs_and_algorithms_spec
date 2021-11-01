# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class BinaryTree:
    key_lower_bound = (-2) ** 31
    key_upper_bound = 2 ** 31 - 1

    def __init__(self):
        def is_key_in_allowed_range():
            if BinaryTree.key_lower_bound <= self.keys[i] <= BinaryTree.key_upper_bound:
                return True
            else:
                return False

        self.res = []
        self.state_str = ''
        self.BST_flag = True

        self.n = int(sys.stdin.readline())
        self.keys = [0 for _ in range(self.n)]
        self.lefts = [0 for _ in range(self.n)]
        self.rights = [0 for _ in range(self.n)]

        for i in range(self.n):
            self.keys[i], self.lefts[i], self.rights[i] = map(int, sys.stdin.readline().split())
            if not is_key_in_allowed_range():
                self.BST_flag = False
                break

        self.sorted_keys = sorted(self.keys)

    # <left><root><right> <=> In-Order <=> СИММЕТРИЧНЫЙ порядок обхода
    def in_order(self, parent_idx=0, current_idx=0):
        def is_left_child():
            if self.lefts[parent_idx] == current_idx:
                return True
            else:
                return False

        def is_right_child():
            if self.rights[parent_idx] == current_idx:
                return True
            else:
                return False

        # BASE case: if a tree or subtree is empty, return
        if current_idx == -1 or self.BST_flag is False:
            return

        # traverse left subtree
        self.in_order(current_idx, self.lefts[current_idx])

        # check if we are in the LEFT subtree and it is consistent with BST rule
        if self.keys[current_idx] >= self.keys[parent_idx] and is_left_child():
            self.BST_flag = False
            return

        # check if we are in the RIGHT subtree and it is consistent with BST rule
        if self.keys[current_idx] < self.keys[parent_idx] and is_right_child():
            self.BST_flag = False
            return

        # if a check succeeds, then visit ROOT node (add its key to resulting array)
        self.res.append(self.keys[current_idx])

        # traverse right subtree
        self.in_order(current_idx, self.rights[current_idx])

    def is_a_BST_base_check(self):
        lst2compare = [key for key in self.res]
        if lst2compare == self.sorted_keys:
            return True
        else:
            return False

    def is_a_BST_advanced_check(self):
        if self.n == 0:
            self.state_str = 'CORRECT'
        else:
            self.in_order()
            if self.BST_flag is True and self.is_a_BST_base_check():
                self.state_str = 'CORRECT'
            else:
                self.state_str = 'INCORRECT'

        print(self.state_str)


def main():
    tree = BinaryTree()
    tree.is_a_BST_advanced_check()


threading.Thread(target=main).start()
