from typing import List


def linear_search(nums: List[int], target: int) -> int:
    len_nums = len(nums)
    for i in range(len_nums):
        if nums[i] == target:
            return i

    return - 1


if __name__ == '__main__':
    target = 2
    nums = [1, 3, 5, 7, 10, 14, 18]
    print(linear_search(nums, target))
