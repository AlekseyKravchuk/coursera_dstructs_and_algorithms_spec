# python3

class Database:
    """
    Simulates a sequence of merge operations with tables in a database.
    Is based on Disjoint Set Union (DSU) with Rank Heuristic and Path Compression Heuristic
    """
    def __init__(self, sizes_lst):
        n = len(sizes_lst)
        self.parent = [i if i != 0 else -1 for i in range(n + 1)]  # store parent of each 'i-th' node
        self.rank = [0 if r != 0 else -1 for r in range(n + 1)]  # store info about heights of corresponding trees
        self.tbl_sizes = [-1] + sizes_lst
        self.max_row_count = max(self.tbl_sizes)

    # DSU 'find' feature with compress path heuristic
    def get_parent(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]

    def merge(self, dst, src):  # dst and src are the corresponding table id
        dst_id, src_id = self.get_parent(dst), self.get_parent(src)

        if dst_id == src_id:
            return False

        if self.rank[dst_id] < self.rank[src_id]:
            self.parent[dst_id] = src_id
            self.tbl_sizes[src_id] += self.tbl_sizes[dst_id]
            self.tbl_sizes[dst_id] = 0
        else:  # self.rank[dst_id] >= self.rank[src_id]
            self.parent[src_id] = dst_id
            self.tbl_sizes[dst_id] += self.tbl_sizes[src_id]
            self.tbl_sizes[src_id] = 0

            if self.rank[dst_id] == self.rank[src_id]:
                self.rank[dst_id] += 1
        self.max_row_count = max(self.max_row_count, self.tbl_sizes[src_id], self.tbl_sizes[dst_id])
        return True


def main():
    n_tables, m_queries = map(int, input().split())
    table_sizes = list(map(int, input().split()))
    assert len(table_sizes) == n_tables

    db = Database(table_sizes)
    for i in range(m_queries):
        dst, src = map(int, input().split())
        db.merge(dst, src)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
