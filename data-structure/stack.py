class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data: int) -> None:
        self.stack.append(data)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    print("######")
    stack.pop()
    print(stack.stack)
