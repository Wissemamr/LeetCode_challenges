from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0

        # Iterate through the list and move non-zero elements to the front
        for idx, num in enumerate(nums):
            if num != 0:
                nums[non_zero_idx], nums[idx] = nums[idx], nums[non_zero_idx]
                non_zero_idx += 1


if __name__ == "__main__":
    sol = Solution()
    test_var = [0, 1, 0, 3, 12]
    print(f"BEFORE : {test_var}")
    sol.moveZeroes(test_var)
    print(f"AFTER : {test_var}")
