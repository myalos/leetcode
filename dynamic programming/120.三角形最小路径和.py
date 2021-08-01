#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 我觉得题目描述里面的相邻节点是i或i + 1这个太棒了
        n = len(triangle)
        for i in range(1, n):
            for j in range(len(triangle[i])):
                # 如果在一层的最左边 那么只能从上一层的最左边下来
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                    continue
                # 如果在一层的最右边 那么只能从上一层的最右边下来
                if j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                    continue
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[n - 1])
# @lc code=end

