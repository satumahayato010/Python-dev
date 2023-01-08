from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        min_idx = i

        for j in range(i+1, len_nums):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(selection_sort(nums))
