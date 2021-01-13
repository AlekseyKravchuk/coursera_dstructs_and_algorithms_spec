from collections import namedtuple


def main():
    VWP = namedtuple('VW', ['value', 'weight', 'per_unit'])
    n, capacity = map(int, input().split())
    items = []
    for i in range(n):
        value, weight = map(int, input().split())
        items.append(VWP(value, weight, value / weight))
    items.sort(reverse=True, key=lambda x: x[2])

    res = 0.0

    for item in items:
        if capacity > 0:
            if item.weight < capacity:
                capacity -= item.weight
                res += item.value
                continue
            elif item.weight == capacity:
                capacity -= item.weight
                res += item.value
                break
            else:  # item.weight > capacity
                res += capacity * item.per_unit
                capacity -= item.weight
                break

    print(f'{res:.4f}')


if __name__ == '__main__':
    main()
