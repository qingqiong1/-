"""
https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked
搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

思路
从右上角开始，这个数是所在行最大值，所在列的最小值
如果这个数小于目标值，说明这一行都小于目标值，应该往下一行寻找，行数加1
同理，大于目标值就是这一列都大于目标值，往前一列找，列数减1

"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 处理空矩阵的边界情况
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)    # 行数
        n = len(matrix[0]) # 列数       
        # 初始化起点：右上角
        row, col = 0, n - 1    
        while row < m and col >= 0:
            current = matrix[row][col]
            if target == current:
                return True
            elif target > current:
                # target更大，向下走，排除当前行
                row += 1
            else:
                # target更小，向左走，排除当前列
                col -= 1
        
        # 越界仍未找到
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
s = Solution()
print(s.searchMatrix(matrix,5))