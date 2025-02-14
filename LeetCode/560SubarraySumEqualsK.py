from typing import List


def summed_array(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        nums[i + 1] += nums[i]
    return nums


def subarray_sum(nums: List[int], k: int) -> List[int]:
    return summed_array(nums)


def main():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    summed = subarray_sum(nums, 4)
    print(list(summed))


if __name__ == '__main__':
    main()
