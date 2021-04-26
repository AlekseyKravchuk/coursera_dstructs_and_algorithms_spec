from math import floor

# For debugging purposes
import sys

def build_heap_min(nums):
    solution = []
    n = len(nums)
    # last element has index start = i = (len(nums)-1), index of it's parent equals to floor((i-1) / 2)
    # we will traverse array in reverse order starting from index 'start' to index with index '0'
    start = floor((n - 2) / 2)

    def heapify_min(i):
        left_idx = 2 * i + 1  # index of left child of current node with index, i
        right_idx = 2 * i + 2  # index of right child of current node with index i

        # Base case
        if left_idx >= n:
            return

        # check if the heap property satisfied, if NO: append corresponding indices, swap numbers
        min_idx = right_idx if right_idx < n and nums[right_idx] <= nums[left_idx] else left_idx
        if nums[i] > nums[min_idx]:
            solution.append((i, min_idx))
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

            if min_idx <= start:  # if min_idx doesn't point to a leaf node
                heapify_min(min_idx)

    for i in range(start, -1, -1):
        heapify_min(i)

    return solution


if __name__ == '__main__':
    # ============== For Debugging ==============
    # in_fname = './tests/04'
    # out_fname = './tests/04.out'
    # with open(in_fname, 'r') as infile, open(out_fname, 'w') as outfile:
    #     sys.stdin = infile
    #     sys.stdout = outfile
    #
    #     n = int(input())
    #     nums = [int(num) for num in input().split()]
    #     assert n == len(nums)
    #     pairs_of_swap_indices = build_heap_min(nums)
    #     print(len(pairs_of_swap_indices))
    #     for pair in pairs_of_swap_indices:
    #         print(*pair)
    # ==========================================

    n = int(input())
    nums = [int(num) for num in input().split()]
    assert n == len(nums)
    pairs_of_swap_indices = build_heap_min(nums)

    print(len(pairs_of_swap_indices))
    for pair in pairs_of_swap_indices:
        print(*pair)

    # ============== For Debugging ==============
    # print resulting array representing proper heap
    # print(nums)
