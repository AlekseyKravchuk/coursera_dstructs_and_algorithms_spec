def mutate_lst(lst):
    print(f'FROM MUTATE_LST: id(lst) = {hex(id(lst))}')
    lst.append(40)
    lst.append(50)
    lst.append(60)


def mutate_lst_recursive(count_lst, res=[]):
    if len(res) > 5:
        return res


if __name__ == '__main__':
    lst = [0] * 4

    # lst = [10, 20, 30]
    # print(f'FROM MAIN: id(lst) = {hex(id(lst))}')
    # # mutate_lst(lst)
    # mutate_lst(lst[:])
    # print(f'lst = {lst}')
