#demonstrate basic problem-solving using breadth-first search on a simple grid.

from collections import deque

grid = [[0,0,0],[1,1,0],[0,0,0]]
start = (0,0)
goal = (2,2)

q = deque([start])
vis = {start}

while q:
    r,c = q.popleft()
    if (r,c) == goal:
        print("Goal reached")
        break
    
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr, c+dc
        if 0<=nr<3 and 0<=nc<3 and grid[nr][nc]==0 and (nr,nc) not in vis:
            q.append((nr,nc))
            vis.add((nr,nc))