"""
Problem: 39. Combination Sum
Url: https://leetcode.com/problems/combination-sum/
Author: David Wang
Date: 06/15/2020
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        sum_sets = []

        self._backtrack(candidates, target, sum_sets)

    def _backtrack(self, candidates, target, sum_sets):
        for c in candidates:
            for s in sum_sets:
