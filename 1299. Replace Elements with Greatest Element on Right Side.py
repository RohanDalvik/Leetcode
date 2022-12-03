class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_ele = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i],curr_ele = curr_ele, max(arr[i],curr_ele)
        return arr