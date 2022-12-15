class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        boats=0 
        r = len(people)-1
        while l<=r:
            remain = limit - people[r]
            r-=1
            boats+=1
            if l<=r and remain >= people[l]:
                l+=1
        return boats