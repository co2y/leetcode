class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inums = [1] + [i for i in nums if i > 0] + [1]
        n = len(inums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          inums[left] * inums[i] * inums[right]
                                          + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
