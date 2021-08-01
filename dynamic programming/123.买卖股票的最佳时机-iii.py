#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 做这道题的时候 已经忘记了前面两个买卖股票的最佳时机的题
        # 最多完成两笔交易, 意思是可以做零笔或者一笔或者两笔
        # 如果在第x天卖出的话，如果当前是第一支股和第二支股的情况是不一样的 第二支
        # 股买入的时间是有限制的
        # 如果这题不放在DP类别的话 我的想法就是如果只买一支股，那么方法就是遍历全部
        # 股票 每遍历到一个股票就记录这个和前面遍历过的所有股票最小值的差，最后取最大值
        # 如果还可以买一个股票的话 那么就是在原来记录中加上一个卖出再买入的操作，卖出的
        # 钱一定是比买入的要大
        
        # 想到把整个数组划分成两个区间，分别对两个区间做最多完成一笔交易的买卖股票
        n = len(prices)  
        # dph[i] 表示在第1到第i支股票最多完成一笔交易条件下能获得的最大利润
        # dpt[i] 表示在第i到最后1支股票最多完成一笔交易条件下能获得的最大利润
        dph, dpt = [0] * (n + 1), [0] * (n + 1)
        _min = prices[0]
        for i in range(2, n + 1):
            _mxprofit = prices[i - 1] - _min
            dph[i] = max(dph[i - 1], _mxprofit)
            _min = min(_min, prices[i - 1])
        _max = prices[n - 1]
        for i in range(n - 1, 1, -1):
            _mxprofit = _max - prices[i - 1]
            dpt[i] = max(dpt[i + 1], _mxprofit)
            _max = max(_max, prices[i - 1])
        # 选择cut点
        res = dph[n]
        for i in range(2, n - 1):
            # 表示卖两次股票 一次是在区间prices[0, ..., i - 1] 另一次是在prices[i, ..., n - 1]
            res = max(res, dph[i] + dpt[i + 1])
        return res
        # 我这个算法只适用于最多可以交易两次，如果最多交易三次，那么我这个算法就不管用了


            
# @lc code=end

for i in range(5, 1, -1):
    print(i)