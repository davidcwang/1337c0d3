"""
Problem: 78. Subsets
Url: https://leetcode.com/problems/subsets/
Author: David Wang
Date: 06/14/2020
"""


class Solution(object):
    # Full and remove
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subset_list = []


        for k in range(len(nums)+1):
            self.backtrack(nums, [], k, subset_list)

        return subset_list


    def backtrack(self, nums, cur, k, subset_list):
        if len(cur) == k:
            return subset_list.append(cur[:])

        for i in range(len(nums)):
            cur.append(nums[i])
            new_nums = nums[0:i] + nums[i+1:]
            self.backtrack(new_nums[:], cur[:], k, subset_list)
            cur.pop()

        for sub in subset_list:
            for n in nums:
                if len(sub) < length:
                    subset_list.append(sub + [n])

    # Empty append
    # def subsets(self, nums):
    #     subset_list = [[]]
    #     self._generate_subsets_recur(nums, 0, [], subset_list)
    #     return subset_list
    #
    # def _generate_subsets_recur(self, nums, start, cur, subset_list):
    #     if start >= len(nums):
    #         return
    #
    #     for i in range(start, len(nums)):
    #         cur.append(nums[i])
    #         subset_list.append(cur[:])
    #         self._generate_subsets_recur(nums, i+1, cur[:], subset_list)
    #         cur.pop()



if __name__ == '__main__':
    input = [1,2,3,]
    output = Solution().subsets(input)
    print(output)
