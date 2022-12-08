class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0=0
        count1=0
        count2=0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0+=1
            elif nums[i] ==1:
                count1+=1
            elif nums[i] ==2:
                count2+=1
        i=0
        while(count0 > 0):
            nums[i] =0
            i+=1
            count0-=1
        while(count1 > 0):
            nums[i] =1
            i+=1
            count1-=1
        while(count2 > 0):
            nums[i]=2
            i+=1
            count2-=1
        return nums