class DisjointSet:
    def __init__(self, size=5):
        self.p = [None]*(size+1)
        self.rank = [None]*(size+1)
        self.size = (size+1)

    def MakeSet(self, i):
        if i >= self.size:
            for i in range(2*i):
                self.p.append(None)
                self.rank.append(None)
        self.p[i] = i
        self.rank[i] = 0

        # print(self.p)
        # print(self.rank)

    def Find(self, i):
        if i != self.p[i]:
            temp = self.Find(self.p[i])
            self.p[i] = temp
        return self.p[i]

    # def Find(self, i):
    #     while i != self.p[i]:
    #         i = self.p[i]
    #     return i

    # with Path Compression Heuristic


    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.p[j_id] = i_id
        else:
            self.p[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[i_id] += 1


if __name__ == '__main__':
    n = 60
    ds = DisjointSet(n)
    for i in range(1, n+1):
        ds.MakeSet(i)
    for i in range(1, 30+1):
        ds.Union(i, 2 * i)
    for i in range(1, 20+1):
        ds.Union(i, 3 * i)
    for i in range(1, 12+1):
        ds.Union(i, 5 * i)
    for i in range(1, 60+1):
        ds.Find(i)
    print(ds.p)
    print(ds.rank)


