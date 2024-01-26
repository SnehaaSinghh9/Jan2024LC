#576. Out of Boundary Paths

#There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
#You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). 
#You can apply at most maxMove moves to the ball.
#Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. 
#Since the answer can be very large, return it modulo 109 + 7.

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves=[(1, 0), (-1,0), (0, 1), (0,-1)]
        @cache
        def f(i, j, moveLeft):
            if i<0 or i==m or j<0 or j==n: return 1
            if moveLeft==0: return 0
            ans=0
            for a, b in moves:
                ans=(ans+f(i+a, j+b, moveLeft-1))%(10**9+7)
            return ans
        return f(startRow, startColumn, maxMove)
