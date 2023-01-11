#/usr/local/bin/python 

'''function that reverses a string. The input string is given as an array of characters s'''
def reverseString(s):
    for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]

# Better, using bitwise not ~x = -x - 1
def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]
    
'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
   value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

def reverse(x):
    d = sum(d * 10 ** i for i,d in enumerate([int(i) if x > 0 else -int(i) for i in str(abs(x)) ]))
    return d if d >= -2**31 and d <= 2 ** 31 - 1 else 0

def reverse(x):
    d = [-1,1][x > 0] * int(str(abs(x))[::-1])
    return d if d >= -2**31 and d <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    s = list("TestString")
    reverseString(s)
    print(s)