 
# Day - 23 Solutions

# Divisible Subset
def find_divisible(arr,k,idx=0,cur = [],s=0):
    if cur and s%k==0:
        return cur[:]
    if idx == len(arr):
        return None
    cur.append(arr[idx])
    res = find_divisible(arr,k,idx+1,cur,s+arr[idx])
    if res:
        return res
    cur.pop()
    return find_divisible(arr,k,idx+1,cur,s)
print(find_divisible([3, 1, 7, 5],6))

# Perfect Squares
def min_sqrs(n):
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        j=1
        while j*j <=i:
            dp[i]= min(dp[i],dp[i- j*j]+1)
            j+=1
    return dp[n]
print(min_sqrs(12))

# Decode String
def decode_str(s):
    stack = []
    curr = ''
    k=0
    for c in s:
        if c.isdigit():
            k = k*10 + int(c)
        elif c=='[':
            stack.append((curr,k))
            curr = ''
            k =0
        elif c == ']':
            prev,times = stack.pop()
            curr = prev + curr*times
        else:
            curr+=c
    return curr
print(decode_str("3[a]2[bc]"))