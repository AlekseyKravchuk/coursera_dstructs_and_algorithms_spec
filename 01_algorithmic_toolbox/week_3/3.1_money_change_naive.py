def main():
    m = int(input())
    num = 0
    denominations = [10, 5, 1]
    while m:
        for _, nominal in enumerate(denominations):
            while m >= nominal:
                m -= nominal
                num += 1
    print(num)


if __name__ == '__main__':
    main()
