if __name__ == '__main__':
    V = ['A', 'B', 'C', 'D']
    print(V)

    # using dict comprehension to map index of vertex to its name
    index_dict = {V[i]: i for i in range(len(V))}
    print(index_dict)
