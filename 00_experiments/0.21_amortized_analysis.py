if __name__ == '__main__':
    # пусть требуемый размер массива - 100 элементов
    n = 10000000
    # При аддитивной схеме перевыделения памяти
    d = 10
    len_lst_additive = len(list(range(1, n, d)))

    # При мультипликативной схеме перевыделения памяти
    q = 2
    curr = 1
    lst_mult = [curr]

    for i in range(n):
        tmp = curr * q
        if tmp < n:
            lst_mult.append(tmp)
            curr = tmp

    print(f'len_lst_additive = {len_lst_additive}\nlen_lst_mult = {len(lst_mult)}')
