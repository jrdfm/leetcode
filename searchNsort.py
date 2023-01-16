#!/usr/local/bin/python 
import unittest

class TestMerge(unittest.TestCase):
    def test_merge(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1,[1,2,2,3,5,6])
        nums1 = [1]
        nums2 = []
        merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1,[1])
        nums1 = [0]
        nums2 = [1]
        merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1,[1])
''' Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and 
    nums2 respectively'''    
def merge(nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
'''Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
   which causes all the following ones to be bad.'''

def isBadVersion(n):
    return True if n >= 4 else False

def firstBadVersion(n):
    low = 1
    high = n
    while low < high:
        mid = low + (high - low) / 2  # to avoid overflow can use m = (l+r)/2 though
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return high

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 # Rounds down

        if arr[mid] > val:
            high = mid - 1

        elif arr[mid] < val:
            low = mid + 1
        
        else:
            return mid

    return -1

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    print(firstBadVersion(5))
