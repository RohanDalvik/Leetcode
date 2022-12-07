class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        aux = collections.Counter(nums)
        n = len(nums)
        for i ,j in aux.items():
            if j > n//2:
                return i