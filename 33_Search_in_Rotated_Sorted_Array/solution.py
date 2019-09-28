"""
Problem: 33. Search in Rotated Sorted Array
Url: https://leetcode.com/problems/search-in-rotated-sorted-array/
Author: David Wang
Date: 09/05/2019
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        return self.rotated_binary_search(0, len(nums)-1, nums, target)

    def rotated_binary_search(self, start, end, array, target):
        if start > end:
            return -1

        mid = int((start + end) / 2)

        if target == array[mid]:
            return mid

        # rotation happens in the left half
        if array[start] > array[mid]:
            # target is in the non-rotated part of the array.
            if target > array[mid] and target <= array[end]:
                return self.rotated_binary_search(mid+1, end, array, target)
            else:
                return self.rotated_binary_search(start, mid-1, array, target)

        # rotation happens on the right half
        else:
            # target is in the non-rotated part of the array.
            if target < array[mid] and target >= array[start]:
                return self.rotated_binary_search(start, mid-1, array, target)
            else:
                return self.rotated_binary_search(mid+1, end, array, target)


if __name__ == '__main__':
    # Test Case 1
    nums = [4,5,6,7,0,1,2]
    target = 4
    output = 0
    res = Solution().search(nums, target)
    assert res == output

    # Test Case 2
    nums = [4,5,6,7,0,1,2]
    target = 3
    output = -1
    res = Solution().search(nums, target)
    assert res == output
