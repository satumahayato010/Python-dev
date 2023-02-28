class Queue(object):

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: int) -> None:
        self.queue.append(data)

    def dequeue(self) -> int:
        if self.queue:
            return self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()
    print(queue.queue)
    queue.enqueue(1)
    print(queue.queue)
    queue.enqueue(2)
    print(queue.queue)
    queue.enqueue(3)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
