#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 因为只能向下或者向右移动一步，所以右下角一定是从上面或者左边移动
        # 过来的，dp的思路的话 dp[3][3] = min(dp[3][2] + 1, dp[2][3] + 1)
        # dp[3][3] = min(dp[3][2], dp[2][3]) + 1
        # 所以只用从右下角开始 看向左还是向上哪个数小 就取哪个数
        # 但是这么做存在一个问题，那就是有些状态下不能向上或向左
        m, n = len(grid), len(grid[0])
        dp = [[1000000] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])
                dp[i][j] += grid[i][j]
        return dp[m - 1][n - 1]



        

# @lc code=end

