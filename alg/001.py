class Solution:
    """
    https://leetcode.com/problems/two-sum/
    """

    def twoSum(self, nums, target):
        hash_map = dict()
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
        # 组合为一个索引序列，同时列出数据和数据下标
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[target - x]]
            hash_map[x] = i


nums = [2, 7, 11, 15]
target = 9
test = Solution()
print(test.twoSum(nums,target))
