#!/usr/local/bin/python
import random
import numpy as np

def binarysearch_nxtsm(A,TARGET):
    L = 0
    R = len(A)-1
    nxs = TARGET
    while L <= R:
        C = (L+R)//2
        print(f'C: {C} SubArr: {A[L:R+1]}')
        if TARGET < A[C]:
            R = C-1
        elif TARGET > A[C]:
            nxs = A[C]
            L = C+1
    return nxs





if __name__ == "__main__":

    # A = [i for i in range(9)] + [i for i in range(10,20)]

    # A = [random.randint(0,50)]
    # print(A)
    # TARGET = 9
    
    # A = random.sample(range(0, 100), 50)
    # A.sort()
    # TARGET = A.pop(random.randint(0,len(A) -1))

    # print(f'TARGET {TARGET}')
    # nx = binarysearch_nxtsm(A,TARGET)

    # print(f'nxs {nx}')
    # print(A)
    # TARGET = A.pop(r := random.randint(0,len(A) -1))
    # print(f'A[r-1] {A[r - 1]}, nxs {binarysearch_nxtsm(A, TARGET)}')

    # for i in range(1000):
    #     TARGET = A.pop(r := random.randint(0,len(A) -1))
    #     print(A[r - 1], binarysearch_nxtsm(A, TARGET))
        # assert(A[r - 1] == binarysearch_nxtsm(A, TARGET))

    B = [3, 5, 8, 9, 12, 13, 16, 19, 21, 24, 26, 27, 30, 35, 36, 37, 38, 42, 45, 
        47, 49, 51, 52, 53, 54, 57, 58, 59, 60, 61, 64, 66, 68, 71, 73, 74, 75, 76, 
        79, 80, 82, 84, 85, 88, 90, 91, 92, 93, 95]

    print(B)
    TARGET = 4
    print(binarysearch_nxtsm(B, TARGET))







