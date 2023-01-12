#!/usr/local/bin/python 

'''function that reverses a string. The input string is given as an array of characters s'''
def reverseString(s):
    for i in range(len(s)//2): 
        s[i], s[-i-1] = s[-i-1], s[i]

# Better, using bitwise not ~x = -x - 1
def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]
    
'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
   value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

def reverse(x):
    d = sum(d * 10 ** i for i,d in enumerate([int(i) if x > 0 else -int(i) for i in str(abs(x)) ]))
    return d if d >= -2**31 and d <= 2 ** 31 - 1 else 0

# Way better
def reverse(x):
    d = [-1,1][x > 0] * int(str(abs(x))[::-1])
    return d if d >= -2**31 and d <= 2 ** 31 - 1 else 0

'''Given a string s, find the first non-repeating character in it and return its index. 
   If it does not exist, return -1.'''

# def firstUniqChar(s):
#     d = {}
#     for i in s:
#         d[i] = d.get(i, 0) + 1
#     for key in d.keys():
#         if d[key] == 1:
#             return s.index(key)
#     return -1        

# Better
def firstUniqChar(s):
    idx = [s.index(i) for i in set(s) if s.count(i) == 1]
    print(set(s))
    print(idx)
    return min(idx) if len(idx) > 0 else -1  

'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''

def isAnagram(s, t):
    sd, td = {}, {}
    for i in s:
        sd[i] = sd.get(i, 0) + 1
    for i in t:
        td[i] = td.get(i, 0) + 1
    return sd == td

def isAnagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    # s = list("TestString")
    # reverseString(s)
    # print(s)

    # s = "loveleetcode"
    # s = "leetcode"
    # print(firstUniqChar(s))
    s = "anagram"
    t = "nagaram"
    s, t = "aacc", "ccac"
    print(isAnagram(s,t))