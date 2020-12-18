from collections import defaultdict


def compute_tree_height(labels):
    parents = defaultdict(list)
    for i, p_label in enumerate(labels):
        parents[p_label].append(i)
    return (len(parents) - 1) if (len(parents) % 2) else (len(parents))


def main():
    n = int(input())  # number of nodes
    labels = [int(x) for x in input().split()]
    assert n == len(labels)
    print(compute_tree_height(labels))


if __name__ == '__main__':
    main()
