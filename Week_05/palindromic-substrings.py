class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = 1
                    result += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    result += 1
                elif j - i > 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    result += 1
        return result
