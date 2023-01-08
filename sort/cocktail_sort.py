from typing import List


def cocktail_sort(nums: List[int]) -> list[int]:
    len_nums = len(nums)
    swapped = True
    start = 0
    end = len_nums - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True

        start += 1

    return nums


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(cocktail_sort(nums))

    for i in range(1, 5):
        print(i)
