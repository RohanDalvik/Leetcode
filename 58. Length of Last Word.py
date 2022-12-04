class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        li = s.split(" ")
        return len(li[-1])