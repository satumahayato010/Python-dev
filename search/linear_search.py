from typing import List


def linear_search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


if __name__ == '__main__':
    target = 3
    import random
    nums = [random.randint(0, 10) for i in range(10)]
    print(nums)
    print(linear_search(nums, target))
