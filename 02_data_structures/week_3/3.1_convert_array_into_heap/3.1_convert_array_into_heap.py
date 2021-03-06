from math import floor


class MinHeap:
    def __init__(self, nums):
        self.h = nums
        self.solution = []
        self.max_size = len(nums)  # maximum size of array
        self.size = len(nums)      # actual size of heap, i.e. number of elements the heap occupies in the array
        self.first_non_leaf = floor((self.size - 2) / 2)  # index of first non-leaf node

    @staticmethod
    def left_child_idx(i):
        return 2 * i + 1

    @staticmethod
    def right_child_idx(i):
        return 2 * i + 2

    def build_minHeap(self):
        for i in range(self.first_non_leaf, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        min_idx = i
        left = self.left_child_idx(i)
        if left < self.size and self.h[left] < self.h[min_idx]:
            min_idx = left
        right = self.right_child_idx(i)
        if right < self.size and self.h[right] < self.h[min_idx]:
            min_idx = right

        if i != min_idx:
            self.solution.append((i, min_idx))
            self.h[i], self.h[min_idx] = self.h[min_idx], self.h[i]
            if min_idx <= self.first_non_leaf:  # if min_idx doesn't point to a leaf node
                self.sift_down(min_idx)


if __name__ == '__main__':
    n = int(input())
    nums = [int(num) for num in input().split()]
    assert n == len(nums)

    h = MinHeap(nums)
    h.build_minHeap()

    print(len(h.solution))
    for pair in h.solution:
        print(*pair)

