import math

"""
Problem: 338. Counting Bits 
Url: https://leetcode.com/problems/counting-bits/ 
Author: David Wang
Date: 01/02/2019
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bit_map = {0: 0, 1: 1}
        bits = [0]
        for i in range(1, num+1):
            exp = int(math.log(i, 2))
            rem = i - 2**exp
            # num_bits is equal to 1 for the base + num_bits of the remainder
            # e.g. 7 = 2**2 + 3 = 1 + bit_map[3] = 1 + 2 = 3
            num_bits = 1 + bit_map[rem]
            bit_map[i] = num_bits
            bits.append(num_bits)

        return bits

if __name__ == '__main__':
    num = 1 
    s = Solution()
    print(s.countBits(num))
