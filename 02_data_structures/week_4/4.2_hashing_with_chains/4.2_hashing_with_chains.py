import sys


class Query:
    def __init__(self, query):
        self.command = query[0]
        if self.command == 'check':
            self.idx2check = int(query[1])
        else:
            self.str = query[1]


class QueryHandler:
    x = 263
    p = 1000000007

    def __init__(self, m):
        self.m = m  # the number of buckets
        self.table = [None] * self.m

    def get_hash(self, s):
        coeffs = list(map(ord, s[::-1]))  # coefficients of polynomial of degree 'len(s) - 1'
        h = 0

        # calculating polynomial value using Horner's rule
        for i, _ in enumerate(coeffs):
            h = (h * self.x + coeffs[i]) % self.p

        return h % self.m

    @staticmethod
    def read_query():
        return Query(input().split())

    @staticmethod
    def print_search_result(is_found):
        print('yes' if is_found else 'no')

    def print_chain(self, query):
        if self.table[query.idx2check] is not None:
            print(' '.join([s for s in self.table[query.idx2check][::-1] if s != '']))
        else:
            print('')

    def get_str_idx_in_chain(self, s, i):
        for idx, key in enumerate(self.table[i]):
            if key == s:
                return idx
        return -1  # chain doesn't contain string

    def process_query(self, query: Query):
        if query.command == 'check':
            self.print_chain(query)
        else:
            i = self.get_hash(query.str)  # i is the index within table (python's array), calculated by hashing
            chain_exists = False if self.table[i] is None else True
            str_idx_in_chain = self.get_str_idx_in_chain(query.str, i) if chain_exists else -1

            if query.command == 'add':
                if chain_exists:
                    if str_idx_in_chain < 0:  # there is no such string in the given chain (table[i])
                        self.table[i].append(query.str)
                else:  # chain doesn't exist
                    self.table[i] = [query.str]  # add new chain at index i
            elif query.command == 'del':
                if chain_exists and str_idx_in_chain >= 0:
                    self.table[i][str_idx_in_chain] = ''
            elif query.command == 'find':
                self.print_search_result(str_idx_in_chain != -1)
            else:
                sys.exit(f'Not supported operation in query: {query.command}. Exiting ...')

    def process_all_queries(self):
        n = int(input())  # n is the number of queries
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    proc_obj = QueryHandler(int(input()))  # QueryHandler takes the number of available buckets for hash function
    proc_obj.process_all_queries()


# ========== for debugging purposes ==========
# if __name__ == '__main__':
#     in_file_name = './tests/06'
#     out_file_name = './tests/06.out'
#     with open(in_file_name, 'r') as in_file, open(out_file_name, 'w') as out_file:
#         sys.stdin = in_file
#         sys.stdout = out_file
#         proc_obj = QueryHandler(int(input()))  # QueryHandler takes the number of available buckets for hash function
#         proc_obj.process_all_queries()




