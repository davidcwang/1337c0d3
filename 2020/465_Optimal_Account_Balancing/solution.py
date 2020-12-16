"""
Problem: 465. Optimal Account Balancing
Url: https://leetcode.com/problems/optimal-account-balancing/
Author: David Wang
Date: 06/24/2020
"""

from typing import List
import collections


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debts = self._calculate_debts(transactions)
        payments = []
        self._min_transfers(transactions, debts, payments, 0)
        return payments

    def _calculate_debts(self, transactions):
        debts = {}

        for t in transactions:
            loaner, borrower, amount = t

            if loaner not in debts:
                debts[loaner] = 0

            if borrower not in debts:
                debts[borrower] = 0

            debts[loaner] -= amount
            debts[borrower] += amount

        return debts

    def _min_transfers(self, transactions, debts, payments, start):
        while start < len(debts) and debts[start] == 0:
            start += 1

        if start == len(debts):
            return 0

        num_trans = len(transactions)
        for i in range(start+1, len(debts)):

            if debts[i] * debts[start] < 0:
                debts[i] += debts[start]

                if debts[i] > debts[start]:
                    diff = debts[i] - debts[start]
                    payments.append((i, start, diff))
                else:
                    diff = debts[start] - debts[i]
                    payments.append((start, i, diff))

                next_trans = 1+self._min_transfers(transactions, debts,
                                                   payments, start+1)
                print(debts)
                print(payments)
                if num_trans < next_trans:
                    payments.pop()
                else:
                    num_trans = next_trans

                debts[i] -= debts[start]

        return num_trans

    # def minTransfers(self, transactions):
    #     """
    #     :type transactions: List[List[int]]
    #     :rtype: int
    #     """
    #     m = {}
    #
    #     for t in transactions:
    #         if t[0] not in m:
    #             m[t[0]] = 0
    #
    #         if t[1] not in m:
    #             m[t[1]] = 0
    #
    #         m[t[0]] -= t[2]
    #         m[t[1]] += t[2]
    #
    #     debt = list(m.values())
    #
    #     def dfs(s):
    #         while (s < len(debt) and debt[s] == 0):
    #             s += 1
    #         if s == len(debt): return 0
    #
    #         r = float('inf')
    #         for i in range(s + 1, len(debt)):
    #             print((i, debt[i]), (s, debt[s]))
    #             if debt[i] * debt[s] < 0:
    #                 # settle s with i
    #                 debt[i] += debt[s]
    #                 print(debt)
    #                 r = min(r, 1 + dfs(s + 1))
    #                 # backtrack
    #                 debt[i] -= debt[s]
    #         return r
    #
    #     return dfs(0)

if __name__ == '__main__':
    input = [[0,1,10], [2,0,5]]
    output = Solution().minTransfers(input)
    print(output)
