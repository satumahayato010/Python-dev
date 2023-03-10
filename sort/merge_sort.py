from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2
    left = nums[:center]
    right = nums[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
            k += 1
        else:
            nums[k] = right[j]
            j += 1
            k += 1

    while len(left) > i:
        nums[k] = left[i]
        i += 1
        k += 1

    while len(right) > j:
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


if __name__ == '__main__':
    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    print(merge_sort(nums))
