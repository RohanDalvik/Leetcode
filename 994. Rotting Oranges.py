class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time ,fresh =0,0 # to keep track of time and fresh oranges
        ROW = len(grid)
        COL = len(grid[0])
        #use nested loop to itetrate over the grid
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] ==1: #keep track of fresh oranges
                    fresh+=1
                #identify any rotten oranges 
                if grid[r][c]==2:
                    q.append([r,c]) # add their cordinates in queue

        direction =[[0,1],[0,-1],[1,0],[-1,0]]# 4 directions we moving
        while q and fresh >0: # while q is not empty and fresh is greater then 0 then  our loop stop
            # we are popping rotten oranges from queue 
            for i in range(len(q)):
                r,c = q.popleft() #pop it's cordinates
                #we traverse all 4 adjecent spot for the rotten oranges
                for dr , dc in direction:
                    row,col= dr+r,dc+c
                    #if it is outof bound or it is not fresh oranges
                    if(row <0 or row == len(grid) or col <0 or col == len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]= 2 #if it is a fresh oranges and it is inbound we make it rotten
                    q.append([row,col])
                    fresh-=1 #decrement the number of fresh orange
            time+=1 # this multisource bfs so it traverse all adjecent rotten oranges in one go 
        return time if fresh==0 else -1    
