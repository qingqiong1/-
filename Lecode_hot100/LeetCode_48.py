"""
https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
思路：
先做转置，再做左右翻转，就完成了旋转操作
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 第一步：转置矩阵（交换 matrix[i][j] 和 matrix[j][i]）
        for i in range(n):
            # 只遍历 j > i 的上三角区域，避免重复交换
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 第二步：翻转每一行（双指针交换首尾）
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()
s.rotate(matrix)
print(matrix)
# [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]