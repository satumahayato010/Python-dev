from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    def _binary_search_recursive(nums: List[int], target: int,
                                 left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return _binary_search_recursive(nums, target, mid+1, right)
        else:
            return _binary_search_recursive(nums, target, left, mid-1)

    return _binary_search_recursive(nums, target, 0, len(nums)-1)


if __name__ == '__main__':
    target = 3
    import random
    nums = [0, 1, 3, 4, 2, 6, 0, 7, 3, 5]
    print(nums)
    print(binary_search_recursive(nums, target))
