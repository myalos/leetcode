#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 计数，子序列的问题
        # 暴力算法就是
        # dfs(si, ti):
        #     if len(t) == ti:
        #         return 1
        #     if si == len(s) or len(s) - si < len(t) - ti:
        #         return 0
        #     res = 0
        #     if s[si] == t[ti]:
        #         res += dfs(si + 1, ti + 1)
        #     res += dfs(si + 1, ti)    
        #     return res 
        # 带个memory就行了 时间复杂度是O(len(s) * len(t))
        @lru_cache
        def dfs(si, ti):
            # 如果完全匹配
            if len(t) == ti:
                return 1
            if si == len(s) or len(s) - si < len(t) - ti:
                return 0
            res = 0
            if s[si] == t[ti]:
                res += dfs(si + 1, ti + 1)
            res += dfs(si + 1, ti)
            return res
        return dfs(0, 0)
# @lc code=end

