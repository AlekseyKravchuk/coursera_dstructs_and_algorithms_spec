class StackWithMax:
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []

    def push(self, num):
        self.main_stack.append(num)

        if self.aux_stack:
            if num >= self.get_max():
                self.aux_stack.append(num)
        else:  # aux_stack is empty, so the initial value duplicated by default in both stacks
            self.aux_stack.append(num)

    def pop(self):
        assert self.main_stack

        from_main_stack = self.main_stack.pop()

        if from_main_stack == self.get_max():
            return self.aux_stack.pop()
        else:
            return from_main_stack

    def get_max(self):
        assert self.aux_stack
        return self.aux_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    n = int(input())
    for _ in range(n):
        query = input().split()
        if query[0] == 'push':
            stack.push(int(query[1]))
        elif query[0] == 'pop':
            stack.pop()
        elif query[0] == 'max':
            print(stack.get_max())
        else:
            assert 0
