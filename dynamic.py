#!/usr/local/bin/python 
import unittest

class Test(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(climbStairs(2),2)
        self.assertEqual(climbStairs(3),3)



'''You are climbing a staircase. It takes n steps to reach the top.
   Each time you can either climb 1 or 2 steps. In how many distinct ways
   can you climb to the top?'''
def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    unittest.main(verbosity=2)