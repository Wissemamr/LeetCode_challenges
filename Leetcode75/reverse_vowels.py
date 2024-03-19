class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ls = list(s)
        # Extract vowels from ls and reverse their order
        vs = [char for char in ls if char in vowels][::-1]
        vs_i = 0
        for i, char in enumerate(ls):
            if char in vowels:
                ls[i] = vs[vs_i]
                vs_i += 1
        new_word = "".join(ls)
        return new_word


if __name__ == "__main__":
    sol = Solution()
    test_words = ["hello", "leetcode", "aA"]
    for word in test_words:
        print(f"For the word: {word}")
        print(f"The answer is : \n{sol.reverseVowels(word)}")
        print("-----------------")
