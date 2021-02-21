class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        def dfs(queens, xy_diff, xy_sum):
            if len(queens) == n:
                results.append(queens)
                return
            for q in range(n):
                if q not in queens and len(queens) - q not in xy_diff and len(queens) + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [len(queens) - q], xy_sum + [len(queens) + q])
        dfs([], [], [])
        return [["."*j+"Q"+"."*(n-j-1) for j in i] for i in results]