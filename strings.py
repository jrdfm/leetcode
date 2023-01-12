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
    d = sum(d * 10 ** i for i,d in enumerate([int(i) if x > 0 else -int(i) for i in s(abs(x)) ]))
    return d if d >= -2**31 and d <= 2 ** 31 - 1 else 0

# Way better
def reverse(x):
    d = [-1,1][x > 0] * int(s(abs(x))[::-1])
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

# Better?
def isAnagram(s, t):
    return sorted(s) == sorted(t)


'''Valid Palindrome'''
def isPalindrome(s):
    ss = ''.join(i for i in s if i.isalnum()).lower()
    return ss == ss[::-1]

'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer'''

def myAtoi(s):
    INT_MAX =  2147483647
    INT_MIN = -2147483648
    result = 0
    sign = 1
    i = 0
    while i < len(s) and s[i].isspace():
        i += 1
    if len(s) == i:
        return result
    if s[i] == "+" or s[i] == "-": 
        sign = [-1,1][s[i] == "+"]
        i += 1

    while i < len(s) and '0' <= s[i] <= '9':
        if result > (INT_MAX - int(s[i])) / 10:
            return INT_MAX if sign > 0 else INT_MIN
        result = result * 10 + int(s[i])
        i += 1
    return sign * result

'''Given two strings needle and haystack, return the index of the first occurrence 
    of needle in haystack, or -1 if needle is not part of haystack.'''

def strStr(haystack, needle):
    ln = len(needle)
    for i in range(len(haystack) - ln + 1):
        if haystack[i:i+ln] == needle:
            return i
    return -1

if __name__ == '__main__':
    # s = list("TestString")
    # reverseString(s)
    # print(s)

    # s = "loveleetcode"
    # s = "leetcode"
    # print(firstUniqChar(s))
    # s = "anagram"
    # t = "nagaram"
    # s, t = "aacc", "ccac"
    # print(isAnagram(s,t))
    # s = "A man, a plan, a canal: Panama"
    # s = "0P"
    # print(isPalindrome(s))
    # s = "4193 with words"
    # s = "   -42"
    # s = ".words and 987"
    # s = "-91283472332" 
    # s = "3.14159"
    # print(myAtoi(s)) 
    haystack = "sadbutsad"
    needle = "sad"
    # haystack = "leetcode"
    # needle = "leeto"
    # haystack = "l"
    # needle = "l"
    haystack = "mississippi"
    needle = "issip"
    

    print(strStr(haystack, needle))