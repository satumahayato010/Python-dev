from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(1, len_nums):
        temp = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = temp

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(insertion_sort(nums))
