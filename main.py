from typing import List


def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1


def quick_sort(nums: List[int]) -> List[int]:
    def _quick_sort(nums: List[int], low: int, high: int) -> None:
        if low < high:
            partition_idx = partition(nums, low, high)
            _quick_sort(nums, low, partition_idx-1)
            _quick_sort(nums, partition_idx+1, high)

    _quick_sort(nums, 0, len(nums)-1)

    return nums


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 50) for i in range(7)]
    print(quick_sort(nums))
