# https://leetcode.cn/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-100-liked

"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
思路
把第一行和第一列作为标志
通过遍历除第一行所有的数字，来修改第一行第一列的数
"""
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        # 1. 先记录第一行和第一列是否原本就有0
        row0_has_zero = False
        col0_has_zero = False
        
        # 检查第一行
        for j in range(m):
            if matrix[0][j] == 0:
                row0_has_zero = True
                break
        
        # 检查第一列
        for i in range(n):
            if matrix[i][0] == 0:
                col0_has_zero = True
                break
        
        # 2. 用第一行和第一列作为标记，遍历剩余元素
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 标记第i行需要置零
                    matrix[0][j] = 0  # 标记第j列需要置零
        
        # 3. 根据标记置零行（从第2行开始）
        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i][:] = [0] * m
        
        # 4. 根据标记置零列（从第2列开始）
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        
        # 5. 最后处理第一行和第一列
        if row0_has_zero:
            matrix[0][:] = [0] * m
        if col0_has_zero:
            for i in range(n):
                matrix[i][0] = 0
