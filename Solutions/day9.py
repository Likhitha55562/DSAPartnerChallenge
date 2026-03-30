
# Day - 9 Solutions

# Spiral matrix
def spiral_matrix(arr):
    res = []
    while arr:
        res+=arr.pop(0)
        arr = list(zip(*arr))[::-1]
    return res
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))

# Set matrix zero 
def set_zero(arr):
    rows = set()
    cols = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                rows.add(i)
                cols.add(j)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i in rows or j in cols:
                arr[i][j] = 0
    return arr
print(set_zero([[1,1,1],[1,0,1],[1,1,1]]))

# Product of Array Except Self
def product(arr):
    n = len(arr)
    res = [1]*n
    left = 1
    for i in range(n):
        res[i] = left
        left *= arr[i]
    right = 1
    for i in range(n-1,-1,-1):
        res[i] *= right
        right *= arr[i]
    return res
print(product([1,2,3,4]))

# Find First and Last Position of Element in Sorted Array
from bisect import bisect_left, bisect_right
def first_last(arr,target):
    l = bisect_left(arr,target)
    r = bisect_right(arr,target) - 1
    if l<=r and l<len(arr) and arr[l]== target:
        return [l,r]
    return [-1,-1]
print(first_last([5,7,7,8,8,10],6))

# Rotate Array
def rotate(arr,k):
    k%=len(arr)
    arr[:] =  arr[-k:] + arr[:-k] 
    return arr
print(rotate([1,2,3,4,5,6,7],3))

# Square root of x
def sqroot(x):
    lo,hi,ans = 1, x//2,0
    while lo<=hi:
        mid = (lo+hi)//2
        if mid*mid<=x:
            ans = mid
            lo = mid+1
        else:
            hi = mid -1
    return ans
print(sqroot(36))

# Guess Number higher or lower
def guess(num):
    target = 20   # hidden number (you can change this)

    if num == target:
        return 0
    elif num < target:
        return 1
    else:
        return -1
def guess_num(n):
    lo , hi = 1,n
    while lo<=hi:
        mid = (lo+hi)//2
        r = guess(mid)
        if r==0:
            return mid
        elif r == 1:
            lo = mid +1
        else:
            hi = mid -1

print(guess_num(34)) 

# First bad version
bad = 4
def isBadVersion(version):
    return version >= bad
def firstbad(n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1           
    return lo
print(firstbad(6))

# Two sum
def sum_in(arr, tar):
    arr.sort()  # important step
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == tar:
            return [lo, hi]   
        elif s < tar:
            lo += 1
        else:
            hi -= 1
    return -1
print(sum_in([5,3,4,1,2], 8))
