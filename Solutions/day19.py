
# Day - 19 Solutions

# Integer to Roman
def int_to_rom(val):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res = ''
    for v,s in zip(vals,syms):
        while val>=v:
            res+=s
            val-=v
    return res
print(int_to_rom(3749))

# Unique paths
from math import comb
def unq_paths(m,n):
    return comb(m+n-2,m-1)
print(unq_paths(3,2))

# Gray code
def gy_code(a):
    return [i^(i>>1) for i in range(1<<a)]
print(gy_code(2))

# Perfect Squares
def per_sq(n):
    dp =[float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        j=1
        while j*j<=1:
            dp[i]=min(dp[i],dp[i-j*j]+1)
            j+=1
    return dp[n]
print(per_sq(12))

# Next Greater Element
def next_grea(n):
    d =  list(str(n))
    i = len(d) - 2
    while i >= 0 and d[i] >= d[i+1]:
       i -= 1
    if i<0:
        return -1
    j = len(d) - 1
    while d[j] <= d[i]:
       j -= 1
    d[i], d[j] = d[j], d[i]
    d[i+1:] = d[i+1:][::-1]
    res = int(''.join(d))
    return res if res <= 2**31 - 1 else -1
print(next_grea(12))

# Angle between hands of a clock
def cloc_han(hr,mins):
    min_angle = 6 * mins
    hr_angle = 0.5 * (hr%12 * 60 + mins)
    diff = abs(hr_angle - min_angle)
    return min(diff,360-diff)
print(cloc_han(12,30))