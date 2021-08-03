def ref_demo(x):
    print("x =", x, " id =", id(x))
    x.append(222)
    print("x =", x, " id =", id(x))


if __name__ == '__main__':
    x = [111]
    print(f'In main function, BEFORE ref_demo(x) : x = {x}, id = {id(x)}')
    ref_demo(x)
    print(f'In main function, AFTER ref_demo(x): x = {x}, id = {id(x)}')
