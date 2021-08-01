#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        # 感觉这个题比较有意思
        # 不过这个题的动作是切一刀 分两个区间 然后再在每个区间进行递归
        # 这属于区间DP 之前做过的87题也是这样, 87题涉及到两个字符串，而且两个字符串的
        # 子串的起始索引可能会不一样，而这题只有一个字符串
        # n = len(s)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        # for l in range(2, n + 1):
        #   for i in range(1, n + 2 - l):
                # 区间[i, ..., i + l - 1]
        #       dp[i][i + l - 1] = n
                # 首先检查该区间是否为回文字符串
        #       if s[i - 1] == s[i + l - 2] and dp[i + 1][i + l - 2] == 0:
        #           dp[i][i + l - 1] = 0
        #           continue
                # 划分成[i, ... , k] [k + 1, ... , i + l - 1]
                # for k in range(i, i + l - 1):
                #    dp[i][i + l - 1] = min(dp[i][i + l - 1], dp[i][k] + dp[k + 1][i + l - 1] + 1)
                # 这么做会超时
                # 要想着降维

        # return dp[1][n]
        n = len(s)
        # 数组p[i][j] 表示字符子串s[i, ... , j] 是否为回文串
        p = [[False] * (n + 1) for _ in range(n + 1)]
        d = [n] * (n + 1)
        # 数组d[i] 表示字符子串s[1, ..., i]切割成回文串的最小切割次数
        d[1] = 0
        d[0] = -1
        for i in range(1, n + 1):
            p[i][i] = True
            p[i][i - 1] = True
        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                left, right = i, i + l - 1
                if s[left - 1] == s[right - 1] and p[left + 1][right - 1]:
                    p[left][right] = True
        # 这个枚举的是最后一个回文串的位置
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                if p[j][i]:
                    d[i] = min(d[i], 1 + d[j - 1])
        return d[n]