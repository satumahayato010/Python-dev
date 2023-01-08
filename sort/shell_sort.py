from typing import List


def shell_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums // 2

    while gap > 0:
        for i in range(gap, len_nums):
            temp = nums[i]
            j = i

            while j >= gap and nums[j-gap] > temp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp

        gap //= 2

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(shell_sort(nums))
