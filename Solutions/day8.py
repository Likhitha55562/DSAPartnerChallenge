
# Day - 8 solutions

# Build array from permutation
class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]
       
obj = Solution()
print(obj.buildArray([0,2,1,5,3,4]))

# Concatenation of array
def concat(arr):
    return arr + arr 
print(concat([1,2,1]))

# Running sum of array
def run_sum(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    return arr
print(run_sum([1,2,3,4]))

# Richest Customer
def amt(*arr):
    return max(sum(row) for row in arr)
print(amt([1,2],[4,5],[3,5]))

# Shuffle the array
def shuffle(arr):
    n = len(arr)//2
    ans = []
    for i in range(n):
        ans.append(arr[i])
        ans.append(arr[i+n])  
    return ans
print(shuffle([2,5,1,3,4,7]))

# Kids With the Greatest Number of Candies
def candies(arr, extra):
    max_candy = max(arr)
    result = []
    for val in arr:
        result.append(val + extra >= max_candy)  
    return result
print(candies([2,3,5,1,3],3))

# Number of good pairs
def good_pairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr [j] and i<j:
                count+=1

    return count
print(good_pairs([1,2,3,1,1,3]))

# How Many Numbers Are Smaller Than the Current Number
def small_arr(arr):
    sorted_arr = sorted(arr)
    return [sorted_arr.index(n) for n in arr]
print(small_arr([8,1,2,2,3]))

# Create target array in given order
def target_arr(arr,idx):
    target = []
    for i in range(len(arr)):
        target.insert(idx[i],arr[i])
    return target
print(target_arr([0,1,2,3,4],[0,1,2,2,1]))

# Check if the Sentence Is Pangram
def is_pangram(sen):
    return len(set(sen)) == 26

print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))

