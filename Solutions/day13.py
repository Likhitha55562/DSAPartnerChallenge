
# Day - 13 Solutions


# Cycle sort
def cycle_sort(arr):
    i = 0
    while i<len(arr):
        correct = arr[i] - 1
        if arr[i]!=arr[correct]:
            arr[i],arr[correct] = arr[correct],arr[i]
        else:
            i+=1
    return arr
print(cycle_sort([3,1,2]))

# Missing number
def missing_num(arr):
    i = 0
    while i<len(arr):
        correct = arr[i]
        if arr[i]<len(arr) and arr[i]!=arr[correct]:
            arr[i],arr[correct] = arr[correct],arr[i]
        else:
            i+=1
    for i in range(len(arr)):
        if arr[i]!=i:
            return i
    return len(arr)
print(missing_num([3,0,1]))

# Find all numbers disappered in an array
def missing_num_all(arr):
    i = 0
    while i<len(arr):
        correct = arr[i] - 1
        if  arr[i]!=arr[correct]:
            arr[i],arr[correct] = arr[correct],arr[i]
        else:
            i+=1
    return [i+1 for i in range(len(arr)) if arr[i] != i+1]
print(missing_num_all([1,1]))

# Find the duplicate number
def find_duplicate(nums):
    i = 0 
    while i<len(nums):
        if nums[i]!=i+1:
            correct = nums[i] - 1
            if nums[i]!=nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                return nums[i]
        else:
            i+=1
    return -1
print(find_duplicate([1,3,4,2,2]))

# Find all duplicates in an array
def find_all_duplicates(arr):
    i = 0
    while i<len(arr):
        correct = arr[i] - 1
        if  arr[i]!=arr[correct]:
            arr[i],arr[correct] = arr[correct],arr[i]
        else:
            i+=1
    return sorted([arr[i] for i in range(len(arr)) if arr[i] != i+1])
print(find_all_duplicates([4,3,2,7,8,2,3,1]))

# Set mismatch
def mis_match(arr):
    i = 0
    while i<len(arr):
        correct = arr[i] - 1
        if  arr[i]!=arr[correct]:
            arr[i],arr[correct] = arr[correct],arr[i]
        else:
            i+=1
    for i, n in enumerate(arr):
        if n != i+1: return [n, i+1]
print(mis_match([1,2,2,4]))

# First missing positive
def find_pos(arr):
    i = 0
    while i<len(arr):
        correct = arr[i]-1
        if 0<arr[i]<=len(arr) and arr[i]!=arr[correct]:
            arr[i],arr[correct]=arr[correct],arr[i]
        else:
            i+=1
    for i in range(len(arr)):
        if arr[i]!=i+1:
            return i+1
    return len(arr)
print(find_pos([3,4,-1,1]))
