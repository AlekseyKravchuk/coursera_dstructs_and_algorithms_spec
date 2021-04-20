from collections import defaultdict
from collections import deque
from typing import List


def compute_tree_height(nodes: List[int]) -> int:
    parents = defaultdict(list)
    for i, parent in enumerate(nodes):
        parents[parent].append(i)

    q = deque(parents[-1])
    height = 0
    while q:
        for _ in range(len(q)):
            current_parent = q.popleft()
            children = parents[current_parent]
            for child in children:
                q.append(child)
        height += 1
    return height


def main():
    n = int(input())  # number of nodes
    nodes = [int(x) for x in input().split()]
    assert n == len(nodes)
    print(compute_tree_height(nodes))


if __name__ == '__main__':
    main()
