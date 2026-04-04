# https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-100-liked
"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照顺时针螺旋顺序 ，返回矩阵中的所有元素。
思路：设置相应的边界值，从左到右，右到下，下到左，左到上循环即可
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix)    # 行数
        m = len(matrix[0]) # 列数
        res = []
        
        # 初始化四个边界
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        while True:
            # 1. 从左到右遍历上边界
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # 上边界向下收缩
            if top > bottom:
                break
            
            # 2. 从上到下遍历右边界
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1 # 右边界向左收缩
            if left > right:
                break
            
            # 3. 从右到左遍历下边界
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1 # 下边界向上收缩
            if top > bottom:
                break
            
            # 4. 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # 左边界向右收缩
            if left > right:
                break
        
        return res
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s = Solution()
print(s.spiralOrder(matrix=matrix))