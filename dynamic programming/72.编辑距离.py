#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
            首先一个传统的想法就是二维dp
            前面一个维度i表示 word1[0 ... i]的子串
            后面一个维度j表示 word2[0 ... j]的子串
            那么dp[i + 1][j] 与 dp[i][j] 的关系是:
                如果第i + 1个字符和第j个字符相同 dp[i][j - 1]
                如果第i + 1个字符和第j个字符不同 要么删掉i 要么删掉j 要么将第i个字符替换成第j个字符                
        '''
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        #对于一个字符串长度为0的情况
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #如果第i + 1个字符和第j个字符相同 dp[i + 1][j] = dp[i][j - 1] 
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                #如果第i + 1个字符和第j个字符不同 要么删掉i 要么删掉j 要么将第i个字符替换成第j个字符                
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
# @lc code=end

