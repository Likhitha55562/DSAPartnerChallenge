
# Day - 11 Solutions

# First and last position of element
from bisect import bisect_left,bisect_right
def search_ele(nums,target):
    l = bisect_left(nums,target)
    r = bisect_right(nums,target) - 1
    return [l,r] if l<=r and l<len(nums) and nums[l]==target else [-1,-1]
print(search_ele([5,7,7,8,8,10],8))

# Single element in an array
def single_element(arr):
    lo , hi = 0 , len(arr) - 1
    while lo<hi:
        mid=lo+(hi-lo)//2
        if mid%2==1:
            mid-=1
        if arr[mid] == arr[mid+1]:
            lo = mid+2
        else:
            hi = mid
    return arr[lo]
print(single_element([1,1,2,3,3,4,4,8,8]))


# Search in Rotated Sorted Array 
def search_sorted(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    
    return -1
print(search_sorted([4,5,6,7,0,1,2],0))

# Search in Rotated Sorted Array II 
def search(nums,target):
    lo,hi = 0 , len(nums) -1
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if nums[mid] == target:
            return True
        if nums[lo]==nums[mid]==nums[hi]:
            lo+=1
            hi-=1
        elif nums[lo]<nums[mid]:
            if nums[lo]<=target<nums[hi]:
                hi = mid -1
            else:
                lo = mid + 1
        else:
            if nums[mid]<target<nums[hi]:
                lo = mid + 1
            else:
                hi = mid -1
    return False
print(search([2,5,6,0,0,1,2],3))

# Find Minimum in Rotated Sorted Array 
def findMin(arr):
    lo , hi = 0,len(arr)-1
    while lo<hi:
        mid = lo + (hi-lo)//2
        if arr[mid]>arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo]
print(findMin([3,4,5,1,2]))

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
           break
    return arr
print(bubble_sort([3,2,4,1,5]))
