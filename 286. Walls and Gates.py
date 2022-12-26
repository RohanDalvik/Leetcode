#Approch ->Do simulatenously bfs from the gates at same time, so everytime we expand our layer we say ok lets first find all the rooms which are 1 distance away from a gate 
#next let's find all the gate with 2 distance away from gate then next find 3 distance away from gate and we keep doing untill every single position in our grid get visisted
#so once our queue is empty we can stop.
#All we need to do is to initilize our queue with the 2 initial position from the gate and then expanding outwards basically incrementing a distance everytime we
#completing full layer of our bfs that leds to time complexity o(m.n).

Class solution:
	def wallsAndGates(self,rooms: List[List[int]])-> None:
		ROWS,COL = len(grid),len(grid[0])
		visit =set()
		q = deque()

		def addrooms(r,c):
			if (r<0 or r == len(ROWS) or c<0 or c == len(COLS) or (r,c) in visit or rooms[r][c] ==-1):
				return #this is invalid room 
			visit.add((r,c)) #if it is valid then add in set and queue
			q.append([r,c])



		for r in range(ROWS):
			for c in range(COL):
				if room[r][c]==0: #if it is gate
					q.append([r,c])
					visit.add((r,c))
		
		
		distance=0 
		while q:
		#we will go to every single position in queue currently basically this layer of the queue 
		for i in range(len(q)):
			r,c = q.popleft()
			
			rooms[r][c] = distance
			#add every single neighbor for the room
			addrooms(r+1,c)
			addrooms(r-1,c)
			addrooms(r,c+1)
			addrooms(r,c-1)
		distance+=1 # increment the distance everytime we complete the layer


			

	


