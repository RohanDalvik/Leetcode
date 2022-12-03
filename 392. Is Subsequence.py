class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        tpointer=0
        spointer=0
        while(tpointer < len(t)):
            if (t[tpointer] == s[spointer]):
                spointer+=1
            tpointer+=1
            if len(s) == spointer:
                return True
        return False