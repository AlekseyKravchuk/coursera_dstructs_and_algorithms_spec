def fb(pr, rec, B):
    return (1 + B**2) * ((pr * rec) / ((B**2) * pr + rec))


if __name__ == '__main__':
    f_b1 = fb(0.7, 0.8, 2)
    f_b2 = fb(0.8, 0.7, 2)
    print(max(f_b1, f_b2))
