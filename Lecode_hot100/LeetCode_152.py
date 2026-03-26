# https://leetcode.cn/problems/maximum-product-subarray/submissions/712405403/?envType=problem-list-v2&envId=2cktkvj
"""
核心思路：同时维护「最大值」和「最小值」
在加法中，我们只需要维护一个 “当前最大值”。但在乘法中：
如果当前数是正数，乘以之前的最大值会更大。
如果当前数是负数，乘以之前的最小值（负数）反而会得到一个很大的正数。
因此，我们需要同时记录两个状态：
dp_max[i]：以第 i 个元素结尾的最大乘积。
dp_min[i]：以第 i 个元素结尾的最小乘积（为了留给下一个负数 “反转” 用）。

状态转移方程
对于第 i 个元素，最大 / 最小值来源于以下三者之一：
自己单干：子数组只有 nums[i]。
乘以前面的最大值：nums[i] * dp_max[i-1]。
乘以前面的最小值：nums[i] * dp_min[i-1]（负负得正的情况）。
"""
from typing  import List
def maxProduct(nums: list[int]) -> int:
    if not nums:
        return 0

    # 初始化：第一个元素既是最大也是最小
    pre_max = nums[0]
    pre_min = nums[0]
    res = nums[0]  # 全局结果

    # 从第二个元素开始遍历
    for i in range(1, len(nums)):
        curr_num = nums[i]

        # 这里必须同时计算，不能先更新 pre_max 再用新的 pre_max 算 pre_min
        curr_max = max(curr_num, pre_max * curr_num, pre_min * curr_num)
        curr_min = min(curr_num, pre_max * curr_num, pre_min * curr_num)
        # 更新全局最大值
        res = max(res, curr_max)
        # 滚动变量，为下一轮做准备
        pre_max, pre_min = curr_max, curr_min

    return res

# --- 测试用例 ---
if __name__ == "__main__":
    # 测试用例 1：经典正负数交替
    test1 = [2, 3, -2, 4]
    print(f"测试用例 1 结果: {maxProduct(test1)}")  # 预期输出: 6 (2*3)

    # 测试用例 2：包含 0 和负数
    test2 = [-2, 0, -1]
    print(f"测试用例 2 结果: {maxProduct(test2)}")  # 预期输出: 0 (不能选 -2*-1，因为不连续)

    # 测试用例 3：负负得正
    test3 = [-2, 3, -4]
    print(f"测试用例 3 结果: {maxProduct(test3)}")  # 预期输出: 24 (-2*3*-4)