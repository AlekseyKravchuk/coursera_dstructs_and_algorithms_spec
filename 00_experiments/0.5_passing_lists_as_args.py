def mutate_lst(lst):
    print(f'FROM MUTATE_LST: id(lst) = {hex(id(lst))}')
    lst.append(40)
    lst.append(50)
    lst.append(60)


if __name__ == '__main__':
    lst = [10, 20, 30]
    print(f'FROM MAIN: id(lst) = {hex(id(lst))}')
    # mutate_lst(lst)
    mutate_lst(lst[:])
    print(f'lst = {lst}')
