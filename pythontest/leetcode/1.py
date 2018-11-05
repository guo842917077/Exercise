"""
leetcode 第一题  求两个数的和
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建一个集合 用来保存第一次遍历的所有元素
        dict_first = {}
        for index, first_data in enumerate(nums):
            dict_first[index] = first_data

        for key, value in dict_first.items():
            # 计算出下一个目标值 用总和-已经在集合中的值  就可以得到下一个预期元素的值
            complete = target - value
            # 如果求得的下一个元素在集合中 且 两个值不能是同一个，即保证索引不一样
            if complete in nums and nums.index(complete) != key:
                a = [key, nums.index(complete)]
                return a


datas = [3, 2, 4]
tar = 6
sol = Solution()
a = sol.twoSum(datas, tar)

print(a)
