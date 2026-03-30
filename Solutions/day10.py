
# Day - 10 solutions

# Valid perfect square
def isPerfectSquare(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False
print(isPerfectSquare(17))

# Arranging coin
def num_of_rows(n):
    lo, hi = 0 , n
    ans = 0
    while lo<=hi: 
        mid = (lo+hi)//2
        coins = mid * (mid+1) // 2
        if coins<=n:
            ans = mid
            lo +=mid
        else:
            hi-=mid
    return ans
print(num_of_rows(5))


# Find Smallest Letter Greater Than Target
def smallest_letter(arr,tar):
    lo , hi = 0,len(arr)-1
    while lo>=hi:
        mid = (lo + hi)//2
        if arr[mid]<= tar:
            lo+=mid
        else:
            hi-=mid
    return arr[lo%len(arr)]

print(smallest_letter(["c","f","j"],"a"))


# Kth positive integer
def ksmallest(arr,k):
    lo,hi = 0, len(arr) - 1
    while lo<=hi: 
        mid = (lo+hi)//2
        missing = arr[mid] - (mid+1)
        if missing<k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo + k

print(ksmallest([2,3,4,7,11],5))

# Search insert position
def search_insert(arr,k):
    lo , hi = 0 , len(arr)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid]>k:
            lo = mid+1
        else:
            hi = mid - 1
    return lo

print(search_insert([1,3,5,6],5))

# Peak mountain element 
def peak(arr):
    lo , hi = 0 , len(arr) - 1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid]<arr[mid+1]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
print(peak([0,1,0]))  

# Count Negative Numbers in a Sorted Matrix
def Countnegatives(grid):
    r = len(grid) - 1
    c = 0
    count = 0
    while r>=0 and c<len(grid[0]):
        if grid[r][c]<0:
            count+= len(grid[0]) - c 
            r-=1
        else:
            c+=1
    return count
print(Countnegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

# Intersection of Two arrays
def intersect(num1,num2):
    return list(set(num1)& set(num2))
print(intersect([1,2,2,1],[2,2]))

# Intersection of Two arrays-2
def intersect(num1,num2):
    num1.sort()
    num2.sort()
    i, j = 0 , 0
    res = []
    while i<len(num1) and j<len(num2):
        if num1[i] == num2[j]:
            res.append(num1[i])
            i+=1
            j+=1
        elif num1[i]<num2[j]:
            i+=1
        else:
            j+=1
    return res
print(intersect([1,2,2,1],[2,2]))

# Fair candy swap
def candy(num1,num2):
   sum1 = sum(num1)
   sum2 = sum(num2)
   diff = (sum1 - sum2) // 2
   set2 = set(num2)
   for a in num1:
      if a-diff in set2:
         return[a,a-diff]
print(candy([1,1],[2,2]))

# Check If N and Its Double Exist
def check_exists(arr):
    seen = set()
    for val in arr:
        if 2*val in seen or (val%2==0 and val//2 in seen):
            return True
        seen.add(val)
    return False
print(check_exists([1,2,5,3]))




