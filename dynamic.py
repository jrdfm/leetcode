#!/usr/local/bin/python 
import unittest


class Test(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(climbStairs(2),2)
        self.assertEqual(climbStairs(3),3)
    
    def test_maxProfit(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)

    def test_maxSubArray(self):
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray([5,4,-1,7,8]), 23)
        self.assertEqual(maxSubArray([1]),1)

    def test_maxSubArray_dq(self):
        self.assertEqual(maxSubArray_dq([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray_dq([5,4,-1,7,8]), 23)
        self.assertEqual(maxSubArray_dq([1]),1)

    def test_rob(self):
        self.assertEqual(rob([1,2,3,1]), 4)
        self.assertEqual(rob([2,7,9,3,1]), 12)
        self.assertEqual(rob([2,1,1,2]), 4)

'''You are climbing a staircase. It takes n steps to reach the top.
   Each time you can either climb 1 or 2 steps. In how many distinct ways
   can you climb to the top?'''
def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

'''Best Time to Buy and Sell Stock II
   Return the maximum profit you can achieve from this transaction. 
   If you cannot achieve any profit, return 0.'''
def maxProfit(prices):
    mxp = 0
    mn = prices[0]
    for i in prices:
        mn = min(i,mn)
        mxp = max(mxp, i - mn)
    return mxp

'''Given an integer array nums, find the subarray with the largest sum, 
   and return its sum.'''
def maxSubArray(nums):
    mx = 0
    mxf = nums[0]
    for i in nums:
        mx = max(i, i + mx)
        mxf = max(mxf, mx)
    return mxf
# Divide & conquer slow as s
def maxSubArray_dq(nums):
    def mcs(nums,l ,r):
        if l > r: return float('-inf')
        c, lhsum, rhsum, csum = (l + r)//2, 0 , 0, 0 
        for i in range(c-1, l-1, -1):
            lhsum = max(lhsum ,csum := csum + nums[i])
        csum = 0
        for i in range(c+1,r+1):
            rhsum = max(rhsum ,csum := csum + nums[i])
        return max(mcs(nums, l, c-1),mcs(nums, c+1, r), lhsum + nums[c] + rhsum)
    return mcs(nums,0,len(nums) - 1)
                    
'''Given an integer array nums representing the amount of money of each house,
   return the maximum amount of money you can rob tonight without alerting the police'''
def rob(nums):
    cur = last = 0
    for i in nums:
        last, cur = cur, max(last + i, cur)
    return cur

if __name__ == '__main__':
    unittest.main(verbosity=2)
