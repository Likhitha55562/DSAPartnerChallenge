 
# Day - 24 solutions

# Different Ways to Add Parentheses
from functools import lru_cache
def diffWaysToCompute(expression):
    @lru_cache(maxsize=None)
    def solve(exprs):
        res = []
        for i, c in enumerate(exprs):
            if c in '+-*':   # ✅ FIX: check actual operator
                for l in solve(exprs[:i]):
                    for r in solve(exprs[i+1:]):
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        else:
                          res.append(l * r)
        return res if res else [int(exprs)]
    return solve(expression)
print(diffWaysToCompute("2-1-1")) 

# Letter Combinations of a Phone Number
def lettercomb(digits):
    if not digits:
        return []
    phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res = []
    def bt(idx,curr):
        if idx==len(digits):
            res.append(curr)
            return
        for c in phone[digits[idx]]:
            bt(idx+1,curr+c) 
    bt(0,'')
    return res
print(lettercomb("23")) 

# Predict the Winner 
from functools import lru_cache
def predictwin(n):
    @lru_cache(maxsize=None)
    def dp(lo,hi):
        if lo==hi:
            return n[lo]
        pick_left = n[lo]-dp(lo+1,hi)
        pick_right = n[hi]-dp(lo,hi-1)
        return (max(pick_left, pick_right))
    return dp(0, len(n) - 1) >= 0
print(predictwin([1,5,2]))

# Gray Code
def grayCode(self, n):
    if n==1: return [0,1]
    prev = self.grayCode(n-1)
    msb = 1 << (n-1)
    return prev + [msb|x for x in reversed(prev)]