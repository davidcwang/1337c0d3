"""
Problem: 46. Permutations
Url: https://leetcode.com/problems/permutations/
Author: David Wang
Date: 06/10/2020
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_perms = []
        self._get_permuate(nums, all_perms)
        return all_perms

    def _get_permuate(self, nums, all_perms):
        for i, n in enumerate(nums):
            cur_perm = [n]
            new_nums = nums[:i] + nums[i+1:]
            self._permute_recur(new_nums, len(nums), cur_perm, all_perms)

    def _permute_recur(self, nums, perm_size, cur_perm, all_perms):
        if len(cur_perm) == perm_size:
            all_perms.append(cur_perm)
            return

        for i, n in enumerate(nums):
            new_cur = cur_perm[:]
            new_cur.append(n)
            new_nums = nums[:i] + nums[i+1:]
            self._permute_recur(new_nums, perm_size, new_cur, all_perms)


if __name__ == '__main__':
    input = [1,2,3]
    output = Solution().permute(input)
    print(output)

