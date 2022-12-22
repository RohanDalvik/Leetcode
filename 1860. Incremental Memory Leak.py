class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        t = 0
        while 1:
            if memory1 < t and memory2 < t:
                return[t,memory1,memory2]
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t +=1