# python3

from collections import namedtuple
from math import floor

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class MinHeapForParallelProcessing:
    def __init__(self, n_workers):
        # each node in the heap is represented by [i, j] where 'i' is next free time of worker with index 'j'
        self.arr = [[0, i] for i in range(n_workers)]
        self.solution = []
        # self.max_size = len(n_workers)  # maximum allowable size of array
        self.size = n_workers  # actual size of heap, i.e. number of elements the heap occupies in the array
        self.first_non_leaf = floor((self.size - 2) / 2)  # index of first non-leaf node

        # because initially we have: [[0, 1], [0, 2], [0, 3], ..., [0, n]], so the heap property is satisfied
        self.isMinHeap = True

    @staticmethod
    def left_child_idx(i):
        return 2 * i + 1

    @staticmethod
    def right_child_idx(i):
        return 2 * i + 2

    def build_min_heap(self):
        for i in range(self.first_non_leaf, -1, -1):
            self.sift_down(i)

    def get_min(self):
        if self.isMinHeap:
            return self.arr[0]
        else:
            self.build_min_heap()
            return self.arr[0]

    def sift_down(self, i):
        min_idx = i  # initially min_idx = i, that is i is the index of parent node

        left_idx = self.left_child_idx(i)
        if left_idx < self.size:  # if index of LEFT child is valid
            if self.arr[left_idx][0] < self.arr[min_idx][0]:  # if next free time is less than
                min_idx = left_idx
            elif self.arr[left_idx][0] == self.arr[min_idx][0]:   # if next free times are equal
                if self.arr[left_idx][1] < self.arr[min_idx][1]:  # if worker index is less than
                    min_idx = left_idx

        right_idx = self.right_child_idx(i)
        if right_idx < self.size:  # if index of RIGHT child is valid
            if self.arr[right_idx][0] < self.arr[min_idx][0]:  # if worker priority is less than
                min_idx = right_idx
            elif self.arr[right_idx][0] == self.arr[min_idx][0]:  #  if next free times are equal
                if self.arr[right_idx][1] < self.arr[min_idx][1]:
                    min_idx = right_idx

        if i != min_idx:
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            if min_idx <= self.first_non_leaf:  # if min_idx doesn't point to a leaf node
                self.sift_down(min_idx)

    def handle_job(self, time2handle):  # change priority for top element in the min_heap depending on time2handle
        # self.arr[0][1] is worker_id of the top node in the heap
        # self.arr[0][0] is next free time of the top node in the heap, it corresponds to time the worker started at
        self.solution.append(AssignedJob(self.arr[0][1], self.arr[0][0]))
        self.arr[0][0] += time2handle

        self.sift_down(0)


def assign_jobs(n_workers, times2handle):
    h = MinHeapForParallelProcessing(n_workers)

    for time_for_job in times2handle:
        h.handle_job(time_for_job)

    return h.solution


def main():
    n_workers, n_jobs = map(int, input().split())
    times2handle = list(map(int, input().split()))
    assert len(times2handle) == n_jobs

    assigned_jobs = assign_jobs(n_workers, times2handle)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
