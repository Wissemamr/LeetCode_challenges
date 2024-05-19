class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            """euclidean algortihm"""
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.gcdOfStrings("ABCABC", "ABC")
    print(f"The answer is : {answer}")
