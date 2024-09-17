from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    guess = len(nums) // 2
    while left != right:
        if nums[guess] is target:
            return guess
        elif target > nums[guess]:
            left = guess
            guess = guess + guess // 2
        elif target < nums[guess]:
            right = guess
            guess = guess - guess // 2
        return False


def main():
    nums = [1, 2, 5, 8, 9, 11, 17, 18, 19, 24]
    print(search(nums, 19))


if __name__ == '__main__':
    main()
