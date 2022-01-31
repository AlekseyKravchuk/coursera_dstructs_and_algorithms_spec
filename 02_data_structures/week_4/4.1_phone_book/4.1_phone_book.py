class Query:
    def __init__(self, line2parse):
        self.type = line2parse[0]
        self.phone_number = int(line2parse[1])
        if self.type == 'add':
            self.name = line2parse[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def process_queries(queries):
    max_phone_len = 7
    phone_book = [None] * 10 ** max_phone_len
    responses = []
    for q in queries:
        if q.type == 'add':
            phone_book[q.phone_number] = q.id
        elif q.type == 'del':
            if phone_book[q.phone_number] is not None:
                phone_book[q.phone_number] = None
        else:  # q.type == 'find'
            if phone_book[q.phone_number] is not None:
                responses.append(phone_book[q.phone_number])
            else:  # contact with such a name was not found
                responses.append('not found')
    return responses


def output_responses(responses):
    print('\n'.join(responses))


if __name__ == '__main__':
    output_responses(process_queries(read_queries()))
