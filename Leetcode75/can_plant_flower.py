from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        counter = 0
        for i in range(1, len(f) - 1):
            # check if 3 consecutive spots are vailable
            if f[i - 1] == f[i] == f[i + 1] == 0:
                # we plant one flower in the middle
                f[i] = 1
                counter += 1
        return n <= counter


if __name__ == "__main__":
    sol = Solution()
    answer = sol.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(f"THe answer is : \n{answer}")
