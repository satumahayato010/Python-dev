from typing import List


def cocktail_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    swap = True
    start, end = 0, len_nums-1
    while swap:
        swap = False
        for i in range(start, end):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swap = True

        if not swap:
            break

        swap = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swap = True

        start = start + 1

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(cocktail_sort(nums))
