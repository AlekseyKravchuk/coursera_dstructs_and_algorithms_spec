import sys

if __name__ == '__main__':
    in_file_name = '06'
    out_file_name = 'strings_to_be_hashed.txt'
    with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
        sys.stdin = in_file
        sys.stdout = out_file

        m, n = int(input()), int(input())
        for i in range(n):
            query = input().split()
            if query[0] == 'add':
                print(query[1])
