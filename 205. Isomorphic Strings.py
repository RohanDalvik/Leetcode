class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m !=n:
            return False
        aux1 = [0]*26
        aux2 = [0]*26
        for i in range(n):
            aux1[ord(s[i])-ord('a')]+=1
            aux2[ord(t[i])-ord('a')]+=1
        for i in range(n):
            if aux1[ord(s[i])-ord('a')] != aux2[ord(t[i])-ord('a')]:
                return False
        return True
#First, create two arrays of size 256 to store the frequency of the characters of the strings.
#Now traverse the string and store the count of the characters.
#After storing the count, check whether the count of every ith character of both the strings are same or not.