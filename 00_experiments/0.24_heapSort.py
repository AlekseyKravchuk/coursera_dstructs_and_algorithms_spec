from math import floor


class MinHeap:
    def __init__(self, nums):
        self.arr = nums
        self.solution = []
        self.max_size = len(nums)  # maximum size of array
        self.size = len(nums)  # actual size of heap, i.e. number of elements the heap occupies in the array
        self.first_non_leaf = floor((self.size - 2) / 2)  # index of first non-leaf node
        self.isHeap = False

    @staticmethod
    def left_child_idx(i):
        return 2 * i + 1

    @staticmethod
    def right_child_idx(i):
        return 2 * i + 2

    def swap_first_and_last(self):
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]

    def descendingHeapSort(self):
        if not self.isHeap:
            self.build_minHeap()
        for i in range(self.size - 1):
            self.swap_first_and_last()
            self.size -= 1
            self.sift_down(0)

    def build_minHeap(self):
        for i in range(self.first_non_leaf, -1, -1):
            self.sift_down(i)
        self.isHeap = True

    def sift_down(self, i):
        min_idx = i
        left = self.left_child_idx(i)
        if left < self.size and self.arr[left] < self.arr[min_idx]:
            min_idx = left
        right = self.right_child_idx(i)
        if right < self.size and self.arr[right] < self.arr[min_idx]:
            min_idx = right

        if i != min_idx:
            self.solution.append((i, min_idx))
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            if min_idx <= self.first_non_leaf:  # if min_idx doesn't point to a leaf node
                self.sift_down(min_idx)


if __name__ == '__main__':
    n = int(input())
    nums = [int(num) for num in input().split()]
    assert n == len(nums)

    h = MinHeap(nums)
    h.build_minHeap()
    h.descendingHeapSort()
    print(h.arr)

    # print(len(h.solution))
    # for pair in h.solution:
    #     print(*pair)
