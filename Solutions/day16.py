
# Day - 16 Solutions


# Split Two Strings to Make Palindrome 
def check(a,b):
    lo,hi = 0, len(b)-1
    while lo<hi and a[lo]==b[hi]:
        lo+=1
        hi-=1
    return a[lo:hi+1]==a[lo:hi+1][::-1] or b[lo:hi+1]==b[lo:hi+1][::-1]
def check_strs(a,b):
    return check(a,b) or check(b,a)
print(check_strs("x","y"))

# Number of Ways to Split a String 
def num_of_ways(s):
    mod = 10**9+7
    n = len(s)
    ones = s.count('1')
    if ones%3:
        return 0
    if ones == 0:
        return (n-1)*(n-2)//2 % mod
    each = ones//3
    cnt = 0
    gaps = []
    for c in s:
        if c=='1':
            cnt+=1
        if cnt in (each,each*2) and c=='1':
            gaps.append(0)
        elif gaps and cnt in (each, each*2):
            gaps[-1] += 1

    return (gaps[0]+1)*(gaps[1]+1) % mod

print(num_of_ways("10101")) 

# First Uppercase letter in a string
def upper_case(s,i=0):
    if i==len(s):
        return '$'
    if s[i].isupper():
        return s[i]
    return upper_case(s,i+1)
print(upper_case("likhi"))

# Sum Triangle from array
def sum_of_triag(arr):
    if len(arr)==1:
        print(arr)
        return
    next_arr = [arr[i]+arr[i+1] for i in range(len(arr)-1)]
    sum_of_triag(next_arr)
    print(arr)
sum_of_triag([1,2,3,4,5])

# Find Maximum and Minimum in Array using Recursion 
def find_max(arr,i=0):
    if i == len(arr)-1:
        return arr[i]
    return max(arr[i],find_max(arr,i+1))
def find_min(arr,i=0):
    if i == len(arr)-1:
        return arr[i]
    return min(arr[i],find_min(arr,i+1))

print(find_max([1,2,3,4,5]))
print(find_min([1,2,3,4,5]))

# Binary search
def binary_search(arr,lo,hi,target):
    if lo>hi:
        return -1
    mid = (lo+hi)//2
    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        return binary_search(arr,mid+1,hi,target)
    return(arr,lo,mid-1,target)
print(binary_search([2,4,1,5,69],0,5,1))

# Next greater element
def next_greater(num1,num2):
    stack , nge = [] , {}
    for n in num2:
        while stack and stack[-1]<n:
            nge[stack.pop()] = n
        stack.append(n)
    return [nge.get(n,-1) for n in num1]
print(next_greater([4,1,2],[1,3,4,2])) 

# Reverse a string
def rev_str(arr,lo,hi):
    if lo>=hi:
        return
    arr[lo],arr[hi] = arr[hi],arr[lo]
    rev_str(arr,lo+1,hi-1)
    return arr
print(rev_str(["h","e","l","l","o"],0,4))
    
# Print 1 to N Without Loop
def prin_1_N(n):
    if n==0:
        return 
    prin_1_N(n-1)
    print(n)   
prin_1_N(6)
