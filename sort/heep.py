import sys


class Heep(object):

    def __init__(self) -> None:
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def parent_idx(self, idx: int) -> int:
        return idx // 2

    def left_child_idx(self, idx: int) -> int:
        return 2 * idx

    def right_child_idx(self, idx: int) -> int:
        return (2 * idx) + 1

    def swap(self, idx1: int, idx2: int) -> None:
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def heapify_up(self, idx: int) -> None:
        while self.parent_idx(idx) > 0:
            if self.heap[idx] < self.heap[self.parent_idx(idx)]:
                self.swap(idx, self.parent_idx(idx))
            idx = self.parent_idx(idx)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)


if __name__ == '__main__':
    heap = Heep()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    print(heap.heap)
