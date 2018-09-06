"""
Problem: 4. Median of Two Sorted Arrays 
Url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Author: David Wang
Date: 01/09/2018

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Returns the length of the longest substring in the given string.

        Args:
            nums1: Sorted array
            nums2: Sorted array
        Returns:
            The median of the two arrays.
        """
        len1 = len(nums1)
        len2 = len(nums2)
        div1 = int((len1 + len2) / 2)

        # if the index is less than the size of the first list then the first
        # list is greater than the second list, so the first elemement will
        # be in the first list.
        if int(div1 / len1) == 0:
            index1 = div1
            val1 = nums1[index1]
            median = val1
           # need to average between the two median numbers of even length.
           # since we know the first list is larger at this point, the second
           # index will be -1 of the first index if the length is even.
            if (len1 + len2) % 2 == 0:
                index2 = index1 - 1
                val2 = nums1[index2]
                median = (val1 + val2) / 2
        # otherwise we'll index into the second element if both lists are of 
        # equal size, or if the second list is larger.
        else:
            index1 = div1 - len1
            val1 = nums2[index1]
            median = val1
            if (len1 + len2) % 2 == 0:
                # if index1 is 0, then we have to need to get the last element
                # of the first list, since that means the sizes are equal.
                if index1 - 1 < 0:
                    index2 = div1 - 1
                    val2 = nums1[index2]
                # otherwise the second list is larger, which means we should
                # get the value of the previous index in the second list.
                else:
                    index2 = index1 - 1
                    val2 = nums2[index2]
                median = (val1 + val2) / 2

        return median

