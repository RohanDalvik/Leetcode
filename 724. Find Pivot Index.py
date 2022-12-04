class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i, num in enumerate(nums):
            # total is now right sum
            # for index i
            total -= num
            if lsum == total:
                return i
            lsum += num
        # If no equilibrium index found,
        # then return -1
        return -1