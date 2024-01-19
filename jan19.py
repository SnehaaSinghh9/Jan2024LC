#931. Minimum Falling Path Sum

#Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. 
#Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


 class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ans = float('inf')

        dp = [[float('inf') for _ in range(c)] for _ in range(r)]

        for i in range(c):
            ans = min(ans, self.rec(0, i, matrix, dp))

        return ans

    def rec(self, i, j, arr, dp):
        if i == len(arr):
            return 0
        if j < 0 or j >= len(arr[0]):
            return float('inf')

        if dp[i][j] != float('inf'):
            return dp[i][j]

        ops1 = self.rec(i + 1, j - 1, arr, dp)
        ops2 = self.rec(i + 1, j, arr, dp)
        ops3 = self.rec(i + 1, j + 1, arr, dp)

        dp[i][j] = arr[i][j] + min(ops1, min(ops2, ops3))
        return dp[i][j]
        
