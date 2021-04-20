class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    q = Queue()
    for num in nums:
        q.enqueue(num)

    for _ in range(len(nums)):
        print(q.dequeue(), end=' ')
