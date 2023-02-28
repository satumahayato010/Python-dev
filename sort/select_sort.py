from typing import List


def select_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        min_idx = i
        for j in range(i+1, len_nums):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 50) for i in range(6)]
    print(select_sort(nums))
