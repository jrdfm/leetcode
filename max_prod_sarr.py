#!/usr/local/bin/python


from typing import List

def maxProduct(nums: List[int]) -> int:
    cmax = cmin = 1
    r = max(nums)
    for i in nums:
        # print(f'i {i}, cmax {cmax}, cmin {cmin}, r {r}')
        mx = cmax * i
        mn = cmin * i
        cmax = max(mx, mn, i)
        cmin = min(mx, mn, i )
        r = max(r, cmax)
        print(f'i {i}, cmax {cmax}, cmin {cmin}, r {r}')
    return r



if __name__ == "__main__":

    nums = [[2,3,-2,4],[-2,0,-1],[0,2],[-2,3,-4],[-4,-3,-2] ]
    for i in nums:
        print(i)
        print(f'{maxProduct(i)}')