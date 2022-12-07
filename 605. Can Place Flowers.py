class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        aux = [0]+flowerbed +[0]
        for i in range(1,len(aux)-1):
            if aux[i-1]==0 and aux[i+1]==0 and aux[i]==0:
                aux[i]=1
                n-=1
        return n<=0
             