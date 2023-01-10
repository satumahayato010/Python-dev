from typing import List, NewType


IndexNum = NewType('IndexNum', int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> IndexNum:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int,
                       left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1

        mid = (left + right) // 2
        print("mid", mid)
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    target = 3
    import random
    nums = [0, 1, 3, 4, 2, 6, 0, 7, 3, 5]
    print(nums)
    print(binary_search_recursive(nums, target))
