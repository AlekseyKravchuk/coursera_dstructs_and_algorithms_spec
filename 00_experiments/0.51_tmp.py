if __name__ == '__main__':
    fname = '/home/kav/PycharmProjects/coursera_dstructs_and_algorithms_spec/03_graphs/week_4/4.1_tests/test_11.txt'
    lines = [' '.join(map(str, (i, i + 1, 1))) for i in range(1, 240)]
    with open(fname, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

