class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset: #if we found duplicate character in our window then we remove the leftmost character and change the window size
                charset.remove(s[l])
                l+=1
            charset.add(s[r]) #if not duplicate we keep adding in our window
            res = max(res,r-l+1) #determine maximum size of window

        return res