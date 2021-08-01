#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 首先处理边界情况 字符长度只有1
        if len(s1) == 1:
            return s1 == s2
        # 字符长度大于1时的情况
        # 就拿great和rgeat来看，gr和rg匹配且eat和eat匹配 要么 eat和rge匹配
        # 且at和at匹配，这是一种切法 如果存在一种切法 切出来的两段有一种匹配方式
        # 那么这两个字符串就是匹配的
        
        # 每次匹配都是相同长度的 一个维度表长度，一个维度表s1起始点，一个维度表s2起始点
        sz = len(s1)
        dp = [[[False] * (sz + 1) for _ in range(sz + 1)] for _ in range(sz + 1)]
        for i in range(1, sz + 1):
            for j in range(1, sz + 1):
                dp[i][j][1] = True if s1[i - 1] == s2[j - 1] else False
        # dp[i][j][k] 表示字符串s1的第i个字符开始的k个字符 和 字符串s2的第j个字符开始的k个字符是否为扰乱字符串
        # 长度从2开始
        for l in range(2, sz + 1):
            for i in range(1, sz + 1):
                # 如果从索引i开始长度为l的字符子串不存在就跳过
                if i + l - 1 > sz:
                    break
                for j in range(1, sz + 1):
                    # 如果从索引j开始长度为l的字符子串不存在就跳过
                    if j + l - 1 > sz:
                        break
                    # 长度为l 切点就有1, 2,..., l - 1
                    for cut in range(1, l):
                        # 如果a/ bc 与 a b c 相匹配 或者 bc / a 与 a b c相匹配
                        if dp[i][j][cut] and dp[i + cut][j + cut][l - cut] or dp[i][j + l - cut][cut] \
                            and dp[i + cut][j][l - cut]:
                            dp[i][j][l] = True
                            break
        return dp[1][1][sz]
# @lc code=end

sol = Solution()
print(sol.isScramble("abc","bca"))