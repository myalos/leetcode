#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 照常dp，对于有障碍物的地方就跳过
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        # 如果起始位置有障碍物的话，那么该位置的dp值为-1
        dp[0][0] = -1 if obstacleGrid[0][0] else 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                # 如果该位置的值为1的话 说明此处的dp值为-1
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1
                else:
                    # 如果上面有路而且没有障碍物的话
                    if i > 0 and dp[i - 1][j] != -1:
                        dp[i][j] += dp[i - 1][j]
                    # 如果左边有路而且没有障碍物的话
                    if j > 0 and dp[i][j - 1] != -1:
                        dp[i][j] += dp[i][j - 1]
        # 如果目的地上面有障碍物 那么就是0
        return 0 if dp[m - 1][n - 1]  == -1 else dp[m - 1][n - 1]
# @lc code=end

