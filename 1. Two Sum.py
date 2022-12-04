class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = [] #created aux list
        for i, x in enumerate(nums): #assign {index,value} pair in the list
            aux.append([x, i])
        aux.sort()  # Sort arr in increasing order by their values.
        
        left, right = 0, len(aux) - 1
        while left < right:
            sum2 = aux[left][0] + aux[right][0]
            if sum2 == target:
                return [aux[left][1], aux[right][1]]
            elif sum2 > target:
                right -= 1  # Try to decrease sum2
            else:
                left += 1  # Try to increase sum2