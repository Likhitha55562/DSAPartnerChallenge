
# Day - 12 solutions

# Selection sort
def select_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
                arr[i],arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(select_sort([-4,6,0,-1,-98]))

# Insertion sort
def insert_sort(arr):
    for i in range(1,len(arr)):
        key, j = arr[i],i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
print(insert_sort([1-3,4,0,-32]))

# Largest number
from functools import cmp_to_key
def large(num):
    strs = list(map(str,num))
    strs.sort(key = cmp_to_key(lambda a,b: 1 if a+b<b+a else -1))
    return '0' if strs[0] == '0' else  ''.join(strs)
print(large([10,2]))

# Kth largest element
import heapq
def k_largest(nums,k):
    return heapq.nlargest(k,nums)[-1]
print(k_largest([3,2,1,5,6,4],2))

# Duplicate number
def duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast] 
    return slow
print(duplicate([1,3,4,2,2]))

# Find all duplicates in an array
def all_duplicates(arr):
    res = []
    for n in arr:
        idx = abs(n) - 1
        if arr[idx]<0:
            res.append(idx+1)
        else:
            arr[idx] = -arr[idx]
    return res
print(all_duplicates([4,3,2,7,8,2,3,1]))

# Aggressive cows
def aggressive_cows(stalls,cows):
    stalls.sort()
    def can_place(d):
        count,last = 1,stalls[0]
        for s in stalls[1:]:
            if s-last>=d:
                count+=1
                last = s
            if count>=cows:
                return True
        return False
    lo, hi ,ans = 1, stalls[-1]-stalls[0],0
    while lo<=hi:
        mid = (lo+hi)//2
        if can_place(mid):
            ans = mid
            lo = mid+1
        else:
            hi = mid -1
    return ans
print(aggressive_cows([1,2,4,8,9],3))

# Book Allocation
def book_allocat(pages,m):
    def students_needed(limit):
        s,cur = 1,0
        for p in pages:
            if cur+p>limit:
                s+=1
                cur = 0
            cur+=p
        return s
    lo,hi,ans= max(pages),sum(pages),0
    while lo<=hi:
        mid = (lo+hi)//2
        if students_needed(mid)<=m:
            ans = mid
            hi = mid -1
        else:
            lo = mid+1
    return ans
print(book_allocat([12, 34, 67, 90],2))
