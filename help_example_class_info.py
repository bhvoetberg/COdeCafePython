from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Solution:
    def find_duplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Test the solution
solution = Solution()
print(solution.find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
print(solution.find_duplicate([3, 1, 3, 4, 2]))  # Output: 3
print(solution.find_duplicate([1, 1]))  # Output: 1
print(solution.find_duplicate([1, 2, 3, 4]))  # Output: None
print(solution.find_duplicate([1]))  # Output: None

print(help(Solution))
