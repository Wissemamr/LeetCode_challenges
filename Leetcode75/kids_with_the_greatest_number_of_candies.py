from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ls = max(candies)
        parts = [part + extraCandies >= max_ls for part in candies]
        return parts


if __name__ == "__main__":
    sol = Solution()
    answer = sol.kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(f"THe answer is : \n{answer}")
