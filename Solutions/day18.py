
# Day - 18 Solutions

# Decode XORed Array 
def dec_arr(arr,n):
    corr_arr = [n]
    for x in arr:
        corr_arr.append(x^corr_arr[-1])
    return corr_arr
print(dec_arr([1,2,3],1))

# Sum of All Subset XOR Totals
def sum_subsets(nums):
    ord_val = 0
    for num in nums:
        ord_val|=num
    return ord_val << (len(nums)-1)
print(sum_subsets([1,3]))


# Longest Nice String
def longest_nice(s):
    if len(s)<2:
        return ''
    chars = set(s)
    for i,c in enumerate(s):
        if c.upper() not in chars or c.lower() not in chars:
            left = longest_nice(s[:i])
            right = longest_nice(s[i+1:])
            return left if len(left)>=len(right) else right
    return s
print(longest_nice("YazaAay"))

# Subsets
def sub_sets(arr):
    n = len(arr)
    return [[arr[i] for i in range(n) if mask>>i&1] for mask in range(1<<n)]
print(sub_sets([1,2,3]))


# Subsets II 
def sub_sets(nums):
    nums.sort()
    res = []
    def bt(start,cur):
        res.append(cur[:])
        for i in range(start,len(nums)):
            if i>start and nums[i]== nums[i-1]:
                continue
            cur.append(nums[i])     
            bt(i + 1, cur)         
            cur.pop()              
    
    bt(0, [])
    return res
print(sub_sets([1, 2, 2]))

# Single Number II
def single_num(arr):
    res = 0
    for i in range(32):
        bit_sum =0
        for n in arr:
            bit_sum+=(n >> i) & 1   
        if bit_sum % 3 != 0:
            res |= (1 << i)   
    return res
print(single_num([2,2,3,2]))

# Divide Two Integers
def divide(dividend,divisor):
    sign = (-1 if (dividend<0)^(divisor<0) else 1)
    dvd, dvs = abs(dividend), abs(divisor)
    ans = 0
    while dvd>=dvs:
        temp,mul =dvs,1
        while dvd>=(temp<<1):
            temp<<=1
            mul<<=1
        dvd-=temp
        ans+=mul
    return sign*ans
print(divide(10,3))

# Gray Code
def gr_code(n):
    return [i ^ (i>>1) for i in range(1<<n)]
print(gr_code(2))

# Repeated DNA Sequences
def rep_seq(s):
    seen = set()
    dup = set()
    for i in range(len(s)-9):
        sub = s[i:i+10]
        if sub in seen:
            dup.add(sub)
        else:
            seen.add(sub)
    return list(dup)

print(rep_seq("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))