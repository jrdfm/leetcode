#!/usr/local/bin/python

'''Remove Duplicates from Sorted Array'''
def rem_dup(nums):
    u = 1
    for i in range(1,len(nums)):
        if nums[i - 1] != nums[i]:
            nums[u] = nums[i]
            u += 1
    return u, nums

'''Best Time to Buy and Sell Stock II'''
def maxProfit(prices):
    mp = 0
    for i in range(1,len(prices)):
        if (t := prices[i] - prices[i - 1]) > 0:
            mp += t
    return mp    

def maxProfit(prices):
    diffs = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    return sum(x for x in diffs if x > 0)

'''Given an array, rotate the array to the right by k steps,
   where k is non-negative.'''
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums.pop())

def rotate(nums, k):

    k %= len(nums)
    nums[:]= nums[-k:] + nums[:k]

def containsDuplicate(nums):
    dup = set()
    for i in nums:
        if i in dup:
            return True
        else:
            dup.add(i)

from functools import reduce
import operator

'''Given a non-empty array of integers nums, every element 
    appears twice except for one. Find that single one.'''
def singleNumber(nums):
    # ls = []
    # for i in nums:
    #     if i in ls:
    #         ls.remove(i)
    #     else:
    #         ls.append(i)
    # return ls[0]
    return  2*sum(set(nums)) - sum(nums) # better
    # return reduce(operator.xor, nums)
'''Given two integer arrays nums1 and nums2, return an array of their intersection.
 Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''
def intersect(nums1, nums2):
    counts= {i:0 for i in set(nums1)}
    for i in nums1:
        counts[i] += 1
    print(counts)
    res = []
    for i in nums2:
        if i in counts and counts[i] > 0:
            res.append(i)
            counts[i] -= 1  
    return res

import collections
def intersect(nums1, nums2):
    counts= collections.Counter(nums1)
    res = []
    for i in nums2:
        if counts[i] > 0:
            res.append(i)
            counts[i] -= 1
    return res    

'''given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
   Increment the large integer by one and return the resulting array of digits.'''

# def plusOne(digits):
#     dig = sum(d * 10 ** i for i,d in enumerate(digits[::-1])) + 1
#     # l = len(digits)
#     # num = 0 
#     # num = sum(digits[i] * 10 ** (l - 1 - i) for i in range(l))
#     return [(dig % 10 ** (i + 1))// 10 ** i for i in reversed(range(len(str(dig))))]
#     return [int(i) for i in str(dig)]
#     return list(map(int,str(dig)))

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

'''Given an integer array nums, move all 0's to the end of it while maintaining 
    the relative order of the non-zero elements.'''
def moveZeroes(nums):
    z = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[z], nums[i]  = nums[i], nums[z]  
            z += 1

'''Given an array of integers nums and an integer target, return indices of the
   two numbers such that they add up to target.'''
def twoSum(nums, target):
    d = {}
    for i,n in enumerate(nums):
        k = target - n
        if k in d:
            return [d[k],i]
        else:
            d[n] = i



'''Determine if a 9 x 9 Sudoku board is valid'''
def isValidSudoku(board):
    def valid(sub):
        sub = [i for i in sub if i != '.']
        return len(sub) == len(set(sub))
    def row_valid(board):
        for row in board:
            if not valid(row):
                return False
        return True
    def col_valid(board):
        for col in zip(*board):
            if not valid(col):
                return False
        return True
    def square_valid(board):
        idx = (0,3,6)
        for i in idx:
            for j in idx:
                sq = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not valid(sq):
                    return False
        return True
    return row_valid(board) and col_valid(board) and square_valid(board)
            

'''given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)'''

def rotate(matrix):
    i = len(matrix) - 1
    j = 0
    while j < i:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        j+=1
        i-=1 
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        
            
        

        
                        
                    
                

if __name__ == '__main__':
    # nums = [0,0,1,1,1,2,2,3,3,4]
    # print(rem_dup(nums))
    # prices  = [7,1,5,3,6,4]
    # print(maxProfit(prices))
    # prices  = [1,2,3,4,5]
    # print(maxProfit(prices))
    # nums = [1,2,3,4,5,6,7]
    # rotate(nums,3)
    # print(nums)
    # nums = [-1,-100,3,99]
    # k = 2
    # rotate(nums,k)
    # print(nums)
    # nums = [1,1,1,3,3,4,3,2,4,2]
    # print(containsDuplicate(nums))

    # nums = [4,1,2,1,2]
    # print(singleNumber(nums))

    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]
    # print(intersect(nums1,nums2))

    # digits = [4,3,2,1]
    # digits = [4,3,2,9]
    # print(plusOne(digits))
    # nums = [0,1,0,3,12]
    # nums = [1]
    # moveZeroes(nums)
    # print(nums)

    # nums = [3,2,4]
    # nums = [3,3]
    # target = 6
    # twoSum(nums,target)

    # board = [["8","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]

    # board = [["5","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]

    # board = [[".",".",".",".","5",".",".","1","."]
    #         ,[".","4",".","3",".",".",".",".","."]
    #         ,[".",".",".",".",".","3",".",".","1"]
    #         ,["8",".",".",".",".",".",".","2","."]
    #         ,[".",".","2",".","7",".",".",".","."]
    #         ,[".","1","5",".",".",".",".",".","."]
    #         ,[".",".",".",".",".","2",".",".","."]
    #         ,[".","2",".","9",".",".",".",".","."]
    #         ,[".",".","4",".",".",".",".",".","."]]

    # print(isValidSudoku(board))

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)