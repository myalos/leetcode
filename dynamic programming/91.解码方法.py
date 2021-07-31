#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[n]表示字符串1...n 的解码个数 第n个字符要么单独解 要么第n - 1和第n个字符一起解
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2, n + 1):
            # 如果第i个字符不是'0'的话，那么第i个字符单独译码，前面i - 1个字符组成的
            # 字符子串总共有dp[i - 1]种译法
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # 如果第i - 1和第i个字符组成的2个字符 为10到26的数字，那么这两个字符单独译码，
            # 前面i - 2个字符组成的字符子串总共有dp[i - 2]种译法
            if s[i - 2 : i] in (str(x) for x in range(10, 27)):
                dp[i] += dp[i - 2]
        return dp[n]
         
# @lc code=end
sol = Solution()
print(sol.numDecodings("226"))
