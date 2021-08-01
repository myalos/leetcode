#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 这道题有非常类似的题目 就是加法最大子数组
        # 对于加法的情况，不会像乘法一样出现跳转 比如乘法 100 -1 -2 
        # 如果用加法方法的dp的话dp[3] = 2 而非 200
        # 想到一个方法 就是两边做dp 那么对于 100 -1 -2;左到右 100 -1 2 右到左200 2 -2
        # 如果是 -2 100 -1 那么就是 -2 100 -1; -2 100 -1 永远找不到200
        n = len(nums)
        # 再想了一下 如果所有数都是正数的话，那么整个数组就是最大子数组
        dp = [0] * (n + 1)
        # 因为存在当前值是负数 但是乘起来能得到最大值 所以需要有一个记录最小值的数组
        pd = [0] * (n + 1)
        pr = [1] * (n + 1) # 遇到0 0后面一个数就为新的连乘起点
        # dp[i] 表示以第i个数为右端点的乘法最大子数组的乘积
        # pd[i] 表示以第i个数为左端点的乘法最小子数组的乘积
        # pr[i] 表示以第i个数为右端点向左到第一个零 之前所有数的乘积
        dp[0] = pr[0] = pd[0] = 1
        for i in range(1, n + 1):
            if nums[i - 1] == 0: # 遇到零 不管最大还是最小 都为0
                dp[i] = pd[i] = 0
                # 遇到0 最大最小应该都是0, 把pr数组也重制了
                pr[i] = 1
            else:
                dp[i] = max(nums[i - 1], nums[i - 1] * dp[i - 1], nums[i - 1] * pr[i - 1], nums[i - 1] * pd[i - 1])
                pd[i] = min(nums[i - 1], nums[i - 1] * dp[i - 1], nums[i - 1] * pr[i - 1], nums[i - 1] * pd[i - 1])
                pr[i] = pr[i - 1] * nums[i - 1]
        return max(dp[1:])
        # 后来发现不需要用pr数组

# @lc code=end
