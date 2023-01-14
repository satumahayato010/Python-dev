class Queue(object):

    def __init__(self) -> None:
        self.queue = []


    def enqueue(self, data: int) -> None:
        self.queue.append(data)

    
    def dequeue(self) -> int:
        if self.queue:
            return self.queue.pop(0)


