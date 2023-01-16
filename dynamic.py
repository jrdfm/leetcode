#!/usr/local/bin/python 
import unittest

class Test(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(climbStairs(2),2)
        self.assertEqual(climbStairs(3),3)
    
    def test_maxProfit(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)


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


if __name__ == '__main__':
    unittest.main(verbosity=2)