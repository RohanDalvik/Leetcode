class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set() #(middle,outer) atmost 26^2 palindromes
        left =set()
        right = collections.Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            for char in left:
                if char in right and right[char] > 0:
                    result.add((char, s[i]))
            left.add(s[i])
        return len(result)