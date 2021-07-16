#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0] * (n + 1) 
        # 第1层 只有一步一种情况， 第二层有一步一步 两步两种情况
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            # 之后的每一层可以是从前一层走一步到 或者 从前两层走两步到
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        
# @lc code=end

